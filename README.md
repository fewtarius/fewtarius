**Open Source Developer | Systems Engineer | Linux Distribution Architect**

Florida | [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)

---

## About Me

I build operating systems and tools that solve real problems. With over 25 years of open source development experience and more than a decade building Linux distributions, I specialize in embedded systems, handheld gaming devices, power management, configuration management, and creating user-first software that respects privacy and transparency.

My approach is pragmatic: build what's needed, make it work reliably, and keep it maintainable. I focus on creating tools that I need and share them with others just in case they find the work useful too.

---

## Currently Working On

### **Synthetic Autonomic Mind** - Privacy-First AI Tools
Building a suite of AI tools designed to be useful, transparent, and user-controlled:

- **[SAM](https://github.com/SyntheticAutonomicMind/SAM)** - A native macOS AI assistant with voice control, local model support, and persistent memory. Built for my wife, now used by anyone who wants an AI assistant that respects their data.
- **[CLIO](https://github.com/SyntheticAutonomicMind/CLIO)** - Command Line Intelligence Orchestrator. A terminal-first AI coding assistant with real tool execution, built entirely in Perl with zero external dependencies. For developers who prefer `vim` to VSCode.
- **[ALICE](https://github.com/SyntheticAutonomicMind/ALICE)** - Artificial Latent Image Composition Engine. Local Stable Diffusion image generation with OpenAI-compatible API, model management, and privacy controls.

### **Handheld Gaming Tools**
- **[PowerDeck](https://github.com/fewtarius/PowerDeck)** - Advanced power management plugin for Steam Deck and compatible handhelds with TDP control, CPU/GPU frequency management, and per-game profiles.
- **[NetDeck](https://github.com/fewtarius/NetDeck)** - Advanced networking plugin featuring MAC spoofing, WiFi hotspot creation, and internet sharing capabilities.

### **PhotonBBS**
Maintaining **[PhotonBBS](https://github.com/fewtarius/photonbbs)**, a telnet-based BBS and MUD platform written in Perl, keeping the dial-up era alive with Docker deployment and modern hosting. Live at `telnet bbs.terminaltavern.com`.

---

## Notable Projects

### **SteamFork** (2024-2025)
Created and maintained **[SteamFork](https://github.com/SteamFork/distribution)**, a SteamOS-based distribution with expanded hardware compatibility. Brought the Steam Deck experience to handheld gaming PCs from ASUS, Ayaneo, Ayn, GPD, and others, plus miniPCs and desktops. Featured:
- Minimal changes from upstream SteamOS for maximum compatibility
- Atomic distribution with rollback and recovery
- Power management optimizations ported from JELOS
- Support for RGB control, improved fan curves, and dual-boot configurations
- Full SteamOS UI/UX including desktop mode
- Maintained sponsored devices with dedicated testing (ROG Ally, Ayaneo 2S, Loki Max, Flip KB)

Project sunset in April 2025 with clean end-of-life and migration path to official SteamOS.

### **Just Enough Linux OS (JELOS)** (2021-2024)
Created and maintained an immutable Linux distribution for ARM and x86-64 handheld gaming devices. JELOS became one of the most popular custom firmwares for devices like the Anbernic RG351, RG552, Odroid Go Ultra, and Orange Pi 5. The project emphasized:
- Automated CI/CD builds and releases
- Minimal, curated system with RetroArch and EmulationStation
- Community-driven development with over 8,000 commits
- Clean end-of-life with clear migration paths to successor projects

The project completed its mission in 2024, with sources remaining available for the community.

### **HomeLab** (2013-2018)
Built an enterprise-grade configuration management system using Chef for automated infrastructure provisioning and maintenance. The system was forked and used by multiple organizations. Featured:
- Automated Chef server deployment and replication
- PXE-based provisioning infrastructure (Cobbler integration)
- RPM build, signing, and hosting services
- CentOS mirror management
- LDAP integration (JumpCloud), SSL automation (Let's Encrypt), DNS management (Zonomi)
- Security hardening and compliance enforcement
- Slack notification integration
- Self-service infrastructure deployment and destruction

### **Fuduntu Linux** (2010-2013)
Developed **Fuduntu**, a Fedora-based Linux distribution that bridged the gap between Fedora and Ubuntu. Featured:
- GNOME 2 classic desktop experience when Unity and GNOME 3 were controversial
- Optimizations for netbooks and portable computers (Asus Eee PC era)
- Power management innovations including the **Jupiter Power Manager**
- RAM disk optimizations and reduced swappiness for battery life
- Active userbase until development concluded in 2013

Fuduntu is documented on [Wikipedia](https://en.wikipedia.org/wiki/Fuduntu) and [DistroWatch](https://distrowatch.com/fuduntu).

### **Netbook Power Management Tools** (2008-2013)

**Eee PC ACPI Utilities** (2008-2009) - Created utilities for managing ACPI functions on the Asus Eee PC, controlling screen brightness, CPU frequency scaling, and hardware toggles through simple command-line tools.

**Eeebuntu Contributor** (2009-2010) - Maintained Eee PC ACPI Utilities as a contributor to Eeebuntu, an Ubuntu variant optimized for the Asus Eee PC and netbooks, until the project concluded in 2010.

**Jupiter Power Manager** (2010-2013) - Built a comprehensive power management applet for Linux that simplified CPU performance tuning, screen output management, and power profile switching. Featured:
- System tray applet with quick access to power modes
- Support for Asus Super Hybrid Engine
- Screen resolution and output management
- Hardware toggle controls
- Integrated into Fuduntu and adopted by other distributions targeting mobile and netbook hardware

### **The Vanilla Laptop Guide** (Hackintosh era)
Created and maintained **fewtarius.gitbook.io/laptopguide**, an authoritative guide for installing macOS on laptop hardware. The guide became a foundational resource referenced across the Hackintosh community and was forked by Dortania as their official legacy laptop guide. Provided detailed instructions for hardware configuration, ACPI patching, and audio setup that enabled thousands of successful Hackintosh builds.

### **351ELEC** (2020-2021)
Forked EmuELEC to create **351ELEC**, a specialized firmware for Anbernic RG351 series handhelds. The distribution featured:
- FAT32 game partition for easy ROM management
- Optimized EmulationStation configuration
- "Plug and play" user experience
- Foundation for what became JELOS

---

## Open Source Contributions

### **Linux Kernel**
Panel orientation quirks for handheld gaming devices merged into mainline kernel:
- GPD Win 2, Win 3, Win Max 2
- AyaNeo Flip DS, Flip KB
- OneXPlayer Mini (Intel)
- Additional handheld gaming devices

Patches backported to stable kernel releases and included in Oracle Enterprise Linux and other distributions.

### **AppleALC** (Acidanthera/Hackintosh)
Audio codec layout contributions merged upstream:
- ALC285 layout-61 for Lenovo Yoga C740
- ALC285 layout-21 fixes for ThinkPad X1C6
- ALC290 improvements for HP devices
- Ice Lake controller patches

Contributions cited in official AppleALC changelog. Provided audio patching assistance to numerous Hackintosh projects including ThinkPad X1C6/X1C7 builds.

### **SimpleDeckyTDP**
Contributed performance optimizations and hardware support:
- Merged SteamFork fork features upstream (APU optimizations, GPU mode improvements, temperature limits)
- Fixed SMT suspend/wake issues on Ayaneo devices
- Improved ryzenadj parameter handling

### **Additional Contributions**
- **CPUFriendFriend** - Perf Bias configuration support for CPU power management optimization
- **InputPlumber** - Handheld device input support
- Community support and troubleshooting across multiple open source projects

---

## Technical Expertise

### **Operating Systems & Distribution Development**
- Linux distribution architecture (Fedora, Debian, embedded systems)
- Buildroot, and custom build systems
- Package management (RPM, DEB, custom repositories)
- Immutable OS design and atomic updates
- CI/CD automation for OS builds

### **Configuration Management & Infrastructure**
- Chef cookbook development and deployment
- Automated provisioning (PXE, Cobbler)
- LDAP integration and authentication (JumpCloud)
- SSL automation (Let's Encrypt)
- DNS management (Zonomi)
- Security hardening and compliance
- Infrastructure as code

### **Embedded & Handheld Systems**
- ARM SoC development (Rockchip, Amlogic, Allwinner)
- x86-64 handheld gaming devices (AMD Z1/Z2, Intel Core)
- Bootloader configuration (U-Boot, systemd-boot)
- Device tree customization
- GPU frequency management and power optimization

### **Kernel & Low-Level Development**
- Linux kernel contributions (panel orientation quirks)
- Power management subsystems (TDP control, CPU governors)
- sysfs interfaces and hardware control
- Driver configuration and hardware enablement
- ACPI patching and DSDT/SSDT modifications

### **Programming Languages**
- **Perl** - Primary language for system tools (CLIO, PhotonBBS, FusionGS)
- **Ruby** - Configuration management (Chef cookbooks, infrastructure automation, 2013-2018)
- **Swift** - Native macOS development (SAM)
- **Python** - AI integration, system scripting (ALICE, PowerDeck, NetDeck)
- **Shell** - Build systems, automation, system integration
- **C** - Kernel patches, low-level utilities

### **AI & Machine Learning**
- Local LLM integration (llama.cpp, Ollama)
- Stable Diffusion deployment and optimization
- OpenAI API compatibility layers
- RAG (Retrieval-Augmented Generation) implementations
- Privacy-first AI architecture

### **Development Practices**
- Git workflow and version control
- GitHub Actions CI/CD
- Docker containerization
- Open source community management
- Technical documentation and user guides

---

## Tools & Technologies

**Operating Systems:** Linux (Fedora, Debian, SteamOS, Arch), macOS  
**Build Systems:** Buildroot, Make, CMake, Autotools  
**Configuration Management:** Chef  
**Containers:** Docker, systemd-nspawn  
**Hardware Platforms:** ARM (Rockchip, Amlogic, Allwinner), x86-64 (AMD, Intel)  
**Graphics:** Mesa, Vulkan, RetroArch, EmulationStation  
**AI/ML:** Stable Diffusion, llama.cpp, Ollama, OpenAI API, Transformers  
**Version Control:** Git, GitHub  
**Languages:** Perl, Ruby, Swift, Python, Shell, C  

---

## Open Source Philosophy

I believe in:
- **Privacy by design** - Your data stays on your hardware
- **Transparency** - Open source everything, readable code, clear documentation
- **User agency** - Tools should empower users, not restrict them
- **Pragmatic solutions** - Solve real problems, ship working software
- **Community-driven development** - Listen to users, accept contributions, maintain openly
- **Clean project lifecycle** - When projects end, document it clearly and help users migrate

---

## How to Reach Me

- **GitHub:** [@fewtarius](https://github.com/fewtarius)
- **Website:** [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)
- **Email:** Available through GitHub profile
- **Organizations:**
  - [Synthetic Autonomic Mind](https://github.com/SyntheticAutonomicMind)
  - [SteamFork](https://github.com/SteamFork) (archived)
  - [Just Enough Linux OS](https://github.com/JustEnoughLinuxOS) (archived)

