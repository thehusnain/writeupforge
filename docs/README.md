# WriteupForge 📝

Convert raw cybersecurity lab notes into professional, structured Markdown and PDF reports using AI.

**Platform Support**: Windows | Linux | macOS  
**UI Options**: GUI (Graphical) | CLI (Command-line)

---

## 📁 Project Structure

```
writeupforge/
├── docs/                      # 📚 Documentation
│   ├── README.md             # Main guide (this file)
│   ├── QUICKSTART.md         # 5-minute quick start
│   └── CHANGES.md            # Changelog
│
├── scripts/                   # 🔧 Installation & Setup Scripts
│   ├── install-wizard.ps1    # Windows setup wizard (recommended)
│   ├── install-linux.sh      # Linux interactive installer
│   ├── install.py            # Universal Python installer
│   ├── launcher.py           # Application launcher
│   └── setup_env.sh/bat      # Environment setup
│
├── config/                    # ⚙️  Configuration
│   └── .env.template         # Template for API configuration
│
├── utils/                     # 🛠️  Utility Modules
│   ├── github_helper.py      # GitHub API helpers
│   └── linkedin_helper.py    # LinkedIn helpers
│
├── main.py                    # ⌨️  CLI Interface (command-line)
├── main_gui.py                # 🖱️  GUI Interface (graphical)
├── run.py                     # 🚀 Application Launcher
├── ai_handler.py              # 🤖 AI/Groq API Handler
├── pdf_generator.py           # 📄 PDF Generation
├── input_handler.py           # ✅ Input Validation
├── spinner.py                 # ⌛ Loading Animations
│
├── requirements.txt           # Python Dependencies
├── setup.py                   # Python Package Setup
└── .env                       # Configuration (API keys) ⚠️ Keep Secret!
```

---

## ✨ Features

- **🤖 AI-Powered**: Uses Groq's fast and free API
- **🖥️ Multi-Platform**: Works on Windows, Linux, and macOS
- **🖱️ GUI & CLI Modes**: Choose your preferred interface
- **📄 Dual Output**: Generates both Markdown and PDF reports
- **⚡ Fast Setup**: Automated installation scripts
- **🔄 Auto-Updates**: Built-in update checker
- **🎨 Professional Styling**: Beautiful formatted output

---

## 📋 Prerequisites

- **Python 3.8 or higher** ([Download here](https://www.python.org/downloads/))
- **Groq API Key** (Free - [Get it here](https://console.groq.com/keys))
- **Git** (Optional, for cloning - [Download here](https://git-scm.com/))

---

## 🚀 Quick Installation

### ⭐ **Windows Users** - Setup Wizard (Easiest!)

```powershell
# 1. Download & Extract the repository
git clone https://github.com/thehusnain/writeupforge.git
cd writeupforge

# 2. Run the installer
# Right-click: scripts/install-wizard.ps1
# Select: "Run with PowerShell"
# Click "Yes" when prompted (needs admin)
```

The wizard will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create Desktop icon
- ✅ Create Start Menu shortcut
- ✅ Set up `.env` file

---

### ⭐ **Linux / macOS Users** - Global Installation (Simplest!)

#### **Option A: pip (Recommended)**

```bash
# 1. Install from GitHub
pip3 install git+https://github.com/thehusnain/writeupforge.git

# 2. Create config directory & add API key
mkdir -p ~/.writeupforge
cp writeupforge/config/.env.template ~/.writeupforge/.env
nano ~/.writeupforge/.env  # Edit and add your API key

# 3. Run from anywhere
writeupforge           # Start in CLI mode
fgwrite --gui         # Start in GUI mode
```

#### **Option B: pipx (Isolated Environment)**

```bash
# 1. Install pipx (if not already installed)
pip3 install --user pipx

# 2. Install WriteupForge in isolated environment
pipx install git+https://github.com/thehusnain/writeupforge.git

# 3. Create config & add API key
mkdir -p ~/.writeupforge
echo "GROQ_API_KEY=your_api_key_here" > ~/.writeupforge/.env

# 4. Run from anywhere
writeupforge
```

#### **Option C: Interactive Setup**

```bash
# 1. Clone & navigate
git clone https://github.com/thehusnain/writeupforge.git
cd writeupforge

# 2. Run interactive installer
chmod +x scripts/install-linux.sh
./scripts/install-linux.sh

# Choose: 1 (pip), 2 (pipx), or 3 (local venv)
```

---

## ⚙️ Configuration

### Get Your Free Groq API Key

1. Visit [https://console.groq.com/keys](https://console.groq.com/keys)
2. Sign up for free (takes 2 minutes)
3. Click **"Create API Key"**
4. Copy the generated key

### Add API Key to `.env`

**For Windows (Setup Wizard users):**
- The `.env` file was created automatically in your project folder
- Just open it and replace `your_api_key_here` with your actual key

**For Linux / macOS (pip/pipx users):**

```bash
# Method 1: Using nano editor (easiest)
nano ~/.writeupforge/.env
# Add your key and press Ctrl+X, then Y, then Enter

# Method 2: Direct command
mkdir -p ~/.writeupforge  # Create directory if it doesn't exist
echo "GROQ_API_KEY=your_api_key_here" > ~/.writeupforge/.env

# Method 3: Copy template and edit
mkdir -p ~/.writeupforge
cp config/.env.template ~/.writeupforge/.env
nano ~/.writeupforge/.env
```

⚠️ **Important**: Replace `your_api_key_here` with your actual Groq API key!

---

## 🏃 Running the Application

### Windows

```bash
# Method 1: Click Desktop icon (after Setup Wizard)
# Double-click "WriteupForge" on Desktop

# Method 2: Start Menu (after Setup Wizard)
# Start Menu > WriteupForge > WriteupForge

# Method 3: Command line from project folder
python run.py              # Auto-detect (GUI)
python run.py --gui       # Force GUI mode
python run.py --cli       # Force CLI mode
```

### Linux / macOS (pip/pipx)

```bash
# From anywhere (global commands)
writeupforge              # CLI mode (default)
fgwrite                  # Alias for CLI
fgwrite --gui            # GUI mode

# Or from project folder
python3 run.py           # Auto-detect
python3 run.py --gui     # Force GUI
python3 run.py --cli     # Force CLI

# Using application launcher
# Search for "WriteupForge" in your applications menu
```

---

## 💻 Usage

### 🖱️ GUI Mode (Recommended)

1. **Open WriteupForge** (via desktop icon, Start Menu, or command)
2. **Fill in the details:**
   - 📝 **Writeup Title**: Name of your challenge/lab
   - 👤 **Your Name**: Your full name
   - 🎯 **Platform**: Select platform (HackTheBox, TryHackMe, PortSwigger, etc.)
   - ⭐ **Difficulty**: Choose difficulty level (Beginner to Expert)
3. **Paste your lab notes** in the text area
4. **Click ✨ Generate Professional Report**
5. **Output files** automatically saved to `output/` folder

**Tips for best results:**
- Include recon, enumeration, and exploitation steps
- Mention tools you used
- Add flags or proof of exploitation
- Share what you learned

### ⌨️ CLI Mode (Terminal)

```bash
writeupforge --cli
```

The CLI will guide you through:
1. Enter writeup title
2. Enter your name
3. Select platform
4. Select difficulty
5. Paste your notes (type `DONE` when finished)

---

## 📂 Output Files

Generated files save to the `output/` directory:

```
output/
├── Challenge_Name_Writeup.md    # Markdown (edit-friendly)
└── Challenge_Name_Writeup.pdf   # Professional PDF
```

Both files are ready to share or customize!

---

## 🔧 Development / Advanced Setup

**For developers or those who prefer manual setup:**

```bash
# 1. Clone repository
git clone https://github.com/thehusnain/writeupforge.git
cd writeupforge

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
cp config/.env.template .env
# Edit .env and add your Groq API key

# 6. Run
python run.py           # GUI mode
python run.py --cli    # CLI mode
```

---

## 🧹 Uninstallation

### Windows
```powershell
scripts\uninstall.bat
# Or use Start Menu > WriteupForge > Uninstall
```

### Linux / macOS

```bash
# If using pip
pip uninstall writeupforge

# If using pipx
pipx uninstall writeupforge

# If using local venv
deactivate
rm -rf venv

# Clean up config
rm -rf ~/.writeupforge
```

---

## 🐛 Troubleshooting

### ❌ "GROQ_API_KEY not found"

**Solution:**
```bash
# Check if .env file exists and has correct content
cat ~/.writeupforge/.env    # Linux/macOS
type .env                   # Windows

# Make sure directory exists
mkdir -p ~/.writeupforge

# Create .env with key
echo "GROQ_API_KEY=your_key_here" > ~/.writeupforge/.env

# Verify it was created
cat ~/.writeupforge/.env
```

### ❌ "Python not found"

- Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
- For Windows: Check "Add Python to PATH" during installation
- For Linux: `sudo apt-get install python3`

### ❌ "Module not found" error

```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or with virtual environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### ❌ "Permission denied" (Linux/macOS)

```bash
# Make scripts executable
chmod +x scripts/*.sh
chmod +x scripts/launcher.py
```

### ❌ "Setup wizard won't run"

- Windows: Right-click `scripts/install-wizard.ps1`
- Select: "Run with PowerShell"
- Click "Yes" when prompted (needs admin privilege)
- If still not working, open PowerShell as Admin and run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

---

## 📊 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.8 | 3.11+ |
| RAM | 2GB | 4GB+ |
| Disk Space | 500MB | 1GB+ |
| Internet | ✅ Required | ✅ Required |

---

## 📚 Quick Links

- 🚀 [Quick Start Guide](docs/QUICKSTART.md)
- 📝 [Changelog](docs/CHANGES.md)
- 🔑 [Get Groq API Key](https://console.groq.com/keys)
- 📦 [Python Downloads](https://www.python.org/downloads/)
- 🐛 [Report Issues](https://github.com/thehusnain/writeupforge/issues)

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

Found a bug or want to add features? 
- Fork the repository
- Create a feature branch
- Submit a pull request

---

## ❓ FAQ

**Q: Is Groq API really free?**
A: Yes! Groq offers free API access with generous rate limits perfect for this use case.

**Q: Can I use offline?**
A: No, you need internet to use the Groq API for AI generation.

**Q: What if I lose my API key?**
A: Generate a new one at [console.groq.com/keys](https://console.groq.com/keys) and update your `.env` file.

**Q: On which OS does it work?**
A: Windows, Linux, and macOS (Python 3.8+)

**Q: Can I edit the generated files?**
A: Yes! Both Markdown and PDF files can be edited afterwards.

**Q: How do I update to the latest version?**
A: Re-run the installer or use `pip install --upgrade writeupforge`

---

## 📧 Support

- 🐛 [GitHub Issues](https://github.com/thehusnain/writeupforge/issues)
- 💬 [Discussions](https://github.com/thehusnain/writeupforge/discussions)
- 🌐 [GitHub Profile](https://github.com/thehusnain)

---

**Made with ❤️ for cybersecurity enthusiasts**

Happy hacking! 🎯
