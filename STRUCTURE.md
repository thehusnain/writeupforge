# Project Structure Guide

This document explains the folder and file organization of WriteupForge.

## 📁 Folder Organization

```
writeupforge/
├── docs/                      # 📚 Documentation & Guides  
│   ├── README.md             # Complete installation & usage guide
│   ├── QUICKSTART.md         # 5-minute quick start for experts
│   └── CHANGES.md            # Detailed changelog
│
├── scripts/                   # 🔧 Installation & Automation Scripts
│   ├── install-wizard.ps1    # ⭐ Windows PowerShell setup wizard
│   ├── install-linux.sh      # ⭐ Linux interactive installer  
│   ├── install.py            # Universal Python installer
│   ├── launcher.py           # Application launcher utility
│   ├── install_linux.sh      # Alternative Linux installer (legacy)
│   ├── install_windows.ps1   # Alternative Windows installer (legacy)
│   ├── setup_env.sh          # Virtual environment setup (Linux/macOS)
│   ├── setup_env.bat         # Virtual environment setup (Windows)
│   ├── uninstall.bat         # Uninstaller (Windows)
│   ├── uninstall.ps1         # Uninstaller (Windows PowerShell)
│   ├── uninstall_linux.sh    # Uninstaller (Linux/macOS)
│   └── launch.bat            # Batch launcher (Windows)
│
├── config/                    # ⚙️  Configuration & Templates
│   └── .env.template         # Template for .env configuration
│                             # (Copy to project root as .env)
│
├── utils/                     # 🛠️  Utility & Helper Modules
│   ├── __init__.py           # Package initialization
│   ├── github_helper.py      # GitHub API integration helpers
│   └── linkedin_helper.py    # LinkedIn helpers
│
├── output/                    # 📄 Generated Reports (Created at first run)
│   ├── Challenge_Writeup.md  # Generated Markdown files
│   └── Challenge_Writeup.pdf # Generated PDF files
│
├── venv/                      # 🐍 Python Virtual Environment (auto-created)
│                             # (Not version controlled)
│
├── .env                       # ⚠️  API Configuration (DO NOT COMMIT)
│                             # Keep your Groq API key here
│
├── .env.example              # Example .env (safe to commit)
├── .gitignore                # Git ignore rules
├── main.py                    # ⌨️  Command-Line Interface (CLI)
├── main_gui.py                # 🖱️  Graphical User Interface (GUI)
├── run.py                     # 🚀 Application Entry Point & Router
├── ai_handler.py              # 🤖 Groq AI API Handler
├── pdf_generator.py           # 📄 PDF Report Generation
├── input_handler.py           # ✅ User Input Validation & Processing
├── spinner.py                 # ⌛ Loading Animations (6 styles)
├── update_checker.py          # 🔄 Version Update Checking
├── version.py                 # 📌 Version Information
├── icon.png                   # 🎨 Application Icon
├── writeupforge.desktop       # 🖥️  Linux Desktop Entry File
│
├── requirements.txt           # 🔧 Python Dependencies List
├── setup.py                   # 📦 Python Package Setup Configuration
├── MANIFEST.in                # 📋 Package Manifest
├── pyproject.toml             # 🎯 Project Configuration
├── README.md                  # 📖 Main Documentation (root)
├── LICENSE                    # ⚖️  MIT License
└── .git/                      # 🔗 Git Repository (version control)
```

---

## 🎯 Which Files Do What?

### Core Application Files
- **run.py** - Main entry point. Auto-detects OS and launches GUI (Windows) or CLI (Linux/macOS)
- **main.py** - Command-line interface for terminal users
- **main_gui.py** - Graphical interface using customtkinter
- **ai_handler.py** - Handles all Groq API calls and AI operations
- **pdf_generator.py** - Converts Markdown writeups to professional PDF reports
- **input_handler.py** - Validates user input (title, name, platform, difficulty)
- **spinner.py** - Beautiful loading animations (6 different styles)
- **update_checker.py** - Checks for newer versions automatically

### Installation & Setup
- **scripts/install-wizard.ps1** ⭐ - Windows users: Run this with PowerShell (easiest!)
- **scripts/install-linux.sh** ⭐ - Linux/macOS users: Run this for interactive setup
- **scripts/launcher.py** - Launches application from anywhere
- **scripts/setup_env.sh/bat** - Manual virtual environment setup
- **scripts/uninstall.*** - Completely removes the application

### Configuration
- **config/.env.template** - Template showing all available configuration options
- **.env** (root) - Your personal configuration (API keys, settings) - KEEP SECRET!
- **writeupforge.desktop** - Linux application menu entry

### Documentation
- **README.md** (root) - Start here! Complete installation and usage guide
- **docs/README.md** - Same as above (kept in sync)  
- **docs/QUICKSTART.md** - Fast 5-minute setup for experienced users
- **docs/CHANGES.md** - Detailed changelog of all updates

### Utilities
- **utils/github_helper.py** - Helper functions for GitHub integration  
- **utils/linkedin_helper.py** - Helper functions for LinkedIn sharing

---

## 🚀 Quick Navigation

### "I want to..."

**Install WriteupForge**
→ Read `README.md` in root or `docs/README.md`

**Run the application after install**
→ Windows: Click Desktop icon
→ Linux: Run `writeupforge` command or search in applications menu

**Configure my API key**
→ Edit `.env` file in project root or `~/.writeupforge/.env` for global config

**Generate a writeup**
→ Launch app (GUI or CLI) and follow the prompts

**Uninstall everything**
→ Run `scripts/uninstall.bat` (Windows) or `scripts/uninstall_linux.sh` (Linux)

**Check the changelog**
→ Read `docs/CHANGES.md`

**See examples of usage**
→ Read `docs/QUICKSTART.md` (5 minutes) or full `README.md` (complete guide)

**Update the application**
→ Will be checked automatically, or re-run the installer

---

## 📝 Configuration Files

### .env (Secret Configuration)
```env
GROQ_API_KEY=your_api_key_here
# Optional: Set specific model
# GROQ_MODEL=llama-3.1-70b-versatile
```

**Location:**
- Windows: `writeupforge\` folder or `%APPDATA%\writeupforge\`
- Linux/macOS: `~/.writeupforge/.env`

**Never commit this file!** It contains your secret API key.

### setup.py
Configures how the application is installed as a Python package. Used by pip/pipx installers.

### pyproject.toml
Modern Python project configuration. Specifies dependencies, metadata, and build system.

### requirements.txt
Simple list of Python package dependencies. Used when installing manually.

---

## 🔄 File Generation & Outputs

### Generated During Installation
- `venv/` - Python virtual environment (if using local setup)

### Generated on First Run
- `output/` - Folder where all generated writeup reports are saved
- `output/*.md` - Generated Markdown files (editable)
- `output/*.pdf` - Generated PDF reports (formatted)

### Generated on User Request  
The application generates two files per writeup:
1. **Markdown** - Editable text format for further customization
2. **PDF** - Professional formatted report

---

## 🔐 What Not to Commit to Git

These are listed in `.gitignore`:
- `.env` - Contains your secret API key! ⚠️
- `venv/` - Virtual environment (large, platform-specific)
- `__pycache__/` - Python cache files
- `*.pyc` - Compiled Python files
- `output/` - Generated reports (user data)

---

## 📦 Dependency Management

### requirements.txt
Lists all Python packages needed:
- **groq** - Groq AI API client
- **click** - Command-line interface framework
- **customtkinter** - Modern GUI library
- **reportlab** - PDF generation
- **python-dotenv** - Environment variable loading

### Installation Methods & Where Files Go

| Method | Installation Location | Config Location | Commands |
|--------|----------------------|-----------------|----------|
| Windows Wizard | Program Files/AppData | `C:\Users\...\AppData\writeupforge\` | Desktop icon, Start Menu |
| pip (Linux/macOS) | `/usr/local/bin` or `~/.local/bin` | `~/.writeupforge/.env` | `writeupforge` (global) |
| pipx (Linux/macOS) | `~/.local/pipx/venvs/` | `~/.writeupforge/.env` | `writeupforge` (isolated) |
| Local venv | Project folder/venv/ | `project/.env` | `python run.py` |

---

## 🎯 Development Notes

### Adding New Features
1. Modify appropriate file: `main.py` (CLI), `main_gui.py` (GUI), etc.
2. Test with `python run.py`
3. Update docs if new functionality added
4. Commit with clear message

### Project Structure Philosophy
- **Organized by function**, not by type
- **docs/** = All documentation together
- **scripts/** = All installation/setup tools together
- **utils/** = All helper modules together
- **Root** = Only essential application files
- **config/** = Configuration templates

### Why This Structure?
✅ Easier to find things
✅ Users see only what they need
✅ Installers are grouped together
✅ Documentation is centralized
✅ Clear separation of concerns

---

**Last Updated**: April 2, 2026
**Structure Version**: 2.0
