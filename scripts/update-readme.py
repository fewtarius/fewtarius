#!/usr/bin/env python3
"""
update-readme.py - Auto-generate README.md from GitHub API data.

Walks all public orgs and personal repos for the configured user,
and writes README.md.

Usage:
    python3 scripts/update-readme.py [--user USER] [--token TOKEN]

Environment:
    GITHUB_TOKEN or GH_TOKEN - API token (optional, raises rate limit)

Config (scripts/readme-config.json, all fields optional):
    {
      "user": "fewtarius",
      "org_overrides": {
        "SyntheticAutonomicMind": {
          "display": "Synthetic Autonomic Mind",
          "tagline": "Privacy-first AI tools..."
        }
      },
      "repo_overrides": {
        "fewtarius/photonbbs": { "description": "Custom description" }
      },
      "exclude_repos": ["fewtarius/some-repo"],
      "header": "Optional markdown to prepend",
      "footer": "Optional markdown to append"
    }
"""

import json
import os
import sys
import urllib.request
import urllib.error
from collections import defaultdict
from datetime import datetime, timezone


CONFIG_FILE = "scripts/readme-config.json"
OUTPUT_FILE = "README.md"
API_BASE    = "https://api.github.com"

# Repos with these names are never interesting to show
SKIP_REPO_NAMES = {".github", "fewtarius"}


# ──────────────────────────────────────────────────────────
# API helpers
# ──────────────────────────────────────────────────────────

def gh_get(path, token=None, params=None):
    url = f"{API_BASE}{path}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"  WARNING: HTTP {e.code} fetching {url}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  WARNING: {e} fetching {url}", file=sys.stderr)
        return None


def gh_get_all(path, token=None, params=None):
    results = []
    page = 1
    base_params = dict(params or {})
    base_params["per_page"] = 100
    while True:
        base_params["page"] = page
        data = gh_get(path, token=token, params=base_params)
        if not data:
            break
        if isinstance(data, list):
            results.extend(data)
            if len(data) < 100:
                break
        else:
            return data
        page += 1
    return results


# ──────────────────────────────────────────────────────────
# Repo data fetching
# ──────────────────────────────────────────────────────────

def fetch_user_orgs(user, token):
    data = gh_get_all(f"/users/{user}/orgs", token=token)
    return [o["login"] for o in data] if data else []


def fetch_org_info(org, token):
    return gh_get(f"/orgs/{org}", token=token) or {}


def fetch_org_repos(org, token):
    repos = gh_get_all(f"/orgs/{org}/repos", token=token,
                       params={"type": "public", "sort": "updated"})
    return [r for r in (repos or []) if not r.get("fork")]


def fetch_user_repos(user, token):
    repos = gh_get_all(f"/users/{user}/repos", token=token,
                       params={"type": "owner", "sort": "updated"})
    return [r for r in (repos or []) if not r.get("fork")]


def has_user_commits(repo_full_name, user, token):
    """Return True if user has at least one commit in the repo."""
    data = gh_get(f"/repos/{repo_full_name}/commits",
                  token=token,
                  params={"author": user, "per_page": "1"})
    return isinstance(data, list) and len(data) > 0


def fetch_user_forks(user, token):
    repos = gh_get_all(f"/users/{user}/repos", token=token,
                       params={"type": "public", "sort": "pushed"})
    forks = [r for r in (repos or [])
             if r.get("fork") and not r.get("archived")]
    # Only include forks where the user has actually committed
    contributed = []
    for r in forks:
        if has_user_commits(r["full_name"], user, token):
            contributed.append(r)
    return contributed

# ──────────────────────────────────────────────────────────
# Rendering
# ──────────────────────────────────────────────────────────

def repo_description(repo, overrides):
    full_name = repo["full_name"]
    if full_name in overrides and overrides[full_name].get("description"):
        return overrides[full_name]["description"]
    return repo.get("description") or ""


def is_interesting(repo):
    return bool(repo.get("description") or repo.get("stargazers_count", 0) > 0)


def render_fork_table(repos, repo_overrides, exclude):
    """Render forks sorted newest-pushed first, filtered to ones with descriptions."""
    lines = [
        "| Project | Description | Language | Last Updated |",
        "|---------|-------------|----------|--------------|",
    ]

    shown = 0
    # API returns sorted by pushed desc already
    for r in repos:
        full_name = r["full_name"]
        name = r["name"]

        if full_name in exclude or name in SKIP_REPO_NAMES:
            continue
        if not is_interesting(r):
            continue

        desc = repo_description(r, repo_overrides)
        lang = r.get("language") or ""
        url  = r["html_url"]
        pushed = r.get("pushed_at", "")
        last_updated = pushed[:7] if pushed else ""
        lines.append(f"| [{name}]({url}) | {desc} | {lang} | {last_updated} |")
        shown += 1

    if shown == 0:
        return ""
    return "\n".join(lines)


def render_repo_table(repos, repo_overrides, exclude, skip_boring_archived=True):
    lines = [
        "| Project | Description | Language |",
        "|---------|-------------|----------|",
    ]

    def sort_key(r):
        return (r.get("archived", False), -r.get("stargazers_count", 0))

    shown = 0
    for r in sorted(repos, key=sort_key):
        full_name = r["full_name"]
        name = r["name"]

        if full_name in exclude or name in SKIP_REPO_NAMES:
            continue
        if r.get("archived") and skip_boring_archived and not is_interesting(r):
            continue

        desc = repo_description(r, repo_overrides)
        lang = r.get("language") or ""
        url  = r["html_url"]
        archived_tag = " *(archived)*" if r.get("archived") else ""
        lines.append(f"| [{name}{archived_tag}]({url}) | {desc} | {lang} |")
        shown += 1

    if shown == 0:
        return ""
    return "\n".join(lines)


def render_org_subsection(org_d, repo_overrides, exclude):
    info    = org_d["info"]
    repos   = org_d["repos"]
    login   = info["login"]
    display = org_d.get("display") or info.get("name") or login
    url     = info.get("html_url", f"https://github.com/{login}")
    tagline = org_d.get("tagline") or info.get("description") or ""
    archived_at = info.get("archived_at")

    heading = f"### [{display}]({url})"
    if archived_at:
        heading += f" *(archived {archived_at[:4]})*"

    block = [heading]
    if tagline:
        block.append(tagline)

    table = render_repo_table(repos, repo_overrides, exclude,
                              skip_boring_archived=True)
    if table:
        block.append("")
        block.append(table)

    return "\n".join(block)


def render_active_orgs(orgs_data, repo_overrides, exclude):
    active = [o for o in orgs_data if not o["info"].get("archived_at")]
    sections = [render_org_subsection(o, repo_overrides, exclude) for o in active]
    return "\n\n".join(sections)


def render_archived_orgs(orgs_data, repo_overrides, exclude):
    archived = [o for o in orgs_data if o["info"].get("archived_at")]
    # Sort newest to oldest by archived_at date
    archived = sorted(archived, key=lambda o: o["info"].get("archived_at", ""), reverse=True)
    sections = [render_org_subsection(o, repo_overrides, exclude) for o in archived]
    return "\n\n".join(sections)


# ──────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}


def main():
    token = None
    args = sys.argv[1:]
    if "--token" in args:
        token = args[args.index("--token") + 1]
    if not token:
        token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    print("GitHub token: " + ("present" if token else "absent (60 req/hr limit)"))

    config = load_config()
    user = None
    if "--user" in args:
        user = args[args.index("--user") + 1]
    user = user or config.get("user") or "fewtarius"

    org_overrides  = config.get("org_overrides", {})
    repo_overrides = config.get("repo_overrides", {})
    exclude        = set(config.get("exclude_repos", []))
    header         = config.get("header", "")
    footer         = config.get("footer", "")

    if not header and os.path.exists("scripts/readme-header.md"):
        with open("scripts/readme-header.md") as f:
            header = f.read().strip()
    if not footer and os.path.exists("scripts/readme-footer.md"):
        with open("scripts/readme-footer.md") as f:
            footer = f.read().strip()

    # ── Fetch ───────────────────────────────────────────────

    print(f"\nFetching orgs for {user}...")
    org_logins = fetch_user_orgs(user, token)
    print(f"  Found: {', '.join(org_logins)}")

    orgs_data = []
    for login in org_logins:
        print(f"\nFetching {login}...")
        info  = fetch_org_info(login, token)
        repos = fetch_org_repos(login, token)
        print(f"  {len(repos)} source repos, archived={bool(info.get('archived_at'))}")

        override = org_overrides.get(login, {})
        orgs_data.append({
            "info":    info,
            "repos":   repos,
            "display": override.get("display"),
            "tagline": override.get("tagline"),
        })

    print(f"\nFetching personal repos for {user}...")
    personal_repos = fetch_user_repos(user, token)
    print(f"  {len(personal_repos)} source repos")

    print(f"\nFetching personal forks for {user}...")
    personal_forks = fetch_user_forks(user, token)
    print(f"  {len(personal_forks)} active forks")

    # ── Render ──────────────────────────────────────────────
    parts = []

    if header:
        parts.append(header)
        parts.append("")

    parts.append("## Organizations")
    parts.append("")
    active_orgs = render_active_orgs(orgs_data, repo_overrides, exclude)
    if active_orgs:
        parts.append(active_orgs)
        parts.append("")
        parts.append("---")
        parts.append("")

    parts.append("## Software")
    parts.append("")
    parts.append(render_repo_table(personal_repos, repo_overrides, exclude,
                                   skip_boring_archived=True))

    fork_table = render_fork_table(personal_forks, repo_overrides, exclude)
    if fork_table:
        parts.append("")
        parts.append("---")
        parts.append("")
        parts.append("## Forks")
        parts.append("")
        parts.append(fork_table)

    archived_orgs = render_archived_orgs(orgs_data, repo_overrides, exclude)
    if archived_orgs:
        parts.append("")
        parts.append("---")
        parts.append("")
        parts.append("## Archived Organizations")
        parts.append("")
        parts.append(archived_orgs)

    if footer:
        parts.append("")
        parts.append(footer)

    parts.append("")
    output = "\n".join(parts)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output)

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\nWrote {OUTPUT_FILE} ({len(output)} bytes) at {updated}")


if __name__ == "__main__":
    main()
