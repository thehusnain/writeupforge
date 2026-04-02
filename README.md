# WriteupForge

Convert raw cybersecurity lab notes into professional, structured Markdown and PDF reports using AI.

**Platform Support**: Windows | Linux
**UI Options**: GUI (Graphical) | CLI (Command-line)

---

## Getting Your Groq API Key (Required First)

Before you install, you need a free Groq API key:

1. Visit: https://console.groq.com/keys
2. Click "Sign Up" (free account, takes 2 minutes)
3. Click "Create API Key"
4. Copy the key (you'll need it during installation)

**You will be prompted for this key during the installer!**

---

## Installation & Setup

### For Linux Users

Step 1: Clone the repository
```bash
git clone https://github.com/thehusnain/writeupforge.git
cd writeupforge
```

Step 2: Run the installer (creates virtual environment + installs dependencies)
```bash
chmod +x scripts/install-linux.sh
./scripts/install-linux.sh
```

The installer automatically:
[+] Creates Python virtual environment
[+] Activates virtual environment
[+] Installs all dependencies
[+] Prompts for Groq API key and saves to .env

Step 3: Activate virtual environment and run
```bash
source venv/bin/activate
python3 run.py --cli    # Command-line mode
python3 run.py --gui    # Graphical mode
```

**Note:** You must run `source venv/bin/activate` every time before using the app (only once per terminal session)

---

### For Windows Users

Step 1: Clone the repository
```
git clone https://github.com/thehusnain/writeupforge.git
cd writeupforge
```

Step 2: Run the installer
[+] Right-click: scripts/install-wizard.ps1
[+] Select: "Run with PowerShell"
[+] Click "Yes" when prompted (needs admin)

The installer automatically:
[+] Creates virtual environment
[+] Installs all dependencies
[+] Creates .env file
[+] Creates Desktop shortcut

Step 3: Add your API key
[+] Open the .env file in project folder
[+] Add your Groq API key (get it at https://console.groq.com/keys)
[+] Save the file

Step 4: Run the application
[+] Click the Desktop shortcut, OR
[+] Use Start Menu > WriteupForge

---

## How to Use

### Running in CLI Mode
```bash
# If not already activated
source venv/bin/activate

python3 run.py --cli
```
[+] Enter writeup title
[+] Enter your name  
[+] Select platform (HackTheBox, TryHackMe, etc.)
[+] Select difficulty level
[+] Paste your notes (type DONE when finished)

### Running in GUI Mode
```bash
# If not already activated
source venv/bin/activate

python3 run.py --gui
```
[+] Fill in the form with your details
[+] Paste your lab notes
[+] Click "Generate Professional Report"

Reports are saved in: output/ folder

---

## Project Structure

```
writeupforge/
├── scripts/               [Installation & Setup]
│   ├── install-wizard.ps1 [Windows installer]
│   ├── install-linux.sh   [Linux installer]
│   └── uninstall.bat      [Windows uninstall]
├── docs/                  [Documentation]
├── config/                [Config templates]
├── utils/                 [Helper modules]
├── main.py                [CLI mode]
├── main_gui.py            [GUI mode]
├── run.py                 [Application launcher]
├── ai_handler.py          [Groq API]
├── requirements.txt       [Dependencies]
└── .env                   [Your API key]
```

---

## Troubleshooting

### Error: "GROQ_API_KEY not found"

Linux:
```bash
nano .env
# Add: GROQ_API_KEY=your_key_here
```

Windows:
[+] Open .env file in project folder
[+] Add your API key
[+] Save and restart

### Error: "Python not found"

Install Python 3.8+:
- Linux: sudo apt install python3 python3-pip
- Windows: Download from python.org (check "Add to PATH")

### Error: "Module not found"
```bash
pip install -r requirements.txt
```

---

## Getting Your API Key

1. Go to https://console.groq.com/keys
2. Sign up (free account takes 2 minutes)
3. Click "Create API Key"
4. Copy the key
5. Add to your .env file
6. Save and restart

---

## Uninstall

Windows:
```
scripts/uninstall.bat
```

Linux:
```bash
rm -rf writeupforge/
```

---

## Requirements

[+] Python 3.8 or higher
[+] Internet connection
[+] 500MB disk space
[+] Free Groq API key

---

## License

MIT License

---

For issues or questions, visit: https://github.com/thehusnain/writeupforge
