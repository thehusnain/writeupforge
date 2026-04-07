# WriteupForge

**WriteupForge** is a tool that converts your raw notes into professional, structured cybersecurity writeups using AI. Whether you're writing learning notes, CTF solutions, lab writeups, or research documentation, WriteupForge automatically detects the type and structures your content accordingly.

It works on Windows, Linux, and macOS, and generates outputs in **Markdown**, **PDF**, and includes **GitHub-ready README files**.

### ✨ v1.1.0 Features
- 🤖 **Automatic Type Detection** - AI detects writeup type (CTF, Lab, Learning, Research, Exploitation, Tool Guide)
- 📋 **Adaptive Structuring** - Content organized based on detected type
- 📊 **Auto Table Generation** - Creates tables where appropriate
- 📑 **GitHub-Ready Output** - Professional README and organized folder structure
- 📁 **One-Click Push to GitHub** - All files organized and ready to commit

---

## 🛠️ Step 1: Getting Your Free AI API Key

WriteupForge uses Groq's super-fast AI to write the reports. It is completely free!

1. Go to **[console.groq.com/keys](https://console.groq.com/keys)**
2. Click **Create API Key**
3. Copy the key (it starts with `gsk_...`)
4. Save it somewhere safe—you'll need it during installation!

---

## 💻 Step 2: Installation

### ⭐ Quick Install from Organization Repository

**For all users (Linux, macOS, Windows with WSL):**

```bash
# Clone from organization repository
git clone https://github.com/fsociety-pk/writeupforge.git
cd writeupforge

# Install with pip
pip install -e .
```

**Or install directly without cloning:**
```bash
pip install git+https://github.com/fsociety-pk/writeupforge.git
```

---

### For Linux Users (Traditional Method)

1. Open your terminal.
2. Clone this folder and go into it:
   ```bash
   git clone https://github.com/fsociety-pk/writeupforge.git
   cd writeupforge
   ```
3. Run the installer script:
   ```bash
   sudo bash install.sh
   ```
   *Note: During installation, it will ask you to paste the Groq API key you just copied.*
4. **Done!** Open a new terminal and just type:
   ```bash
   fgwrite
   ```

### For Windows Users

1. Download and extract this project folder.
2. Search for **PowerShell** in the Start Menu, right-click it, and select **Run as Administrator**.
3. Go to the extracted folder in PowerShell:
   ```powershell
   cd path\to\writeupforge
   ```
4. Run the installer:
   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts\install-wizard.ps1
   ```
   *Note: Just like Linux, it will ask for your Groq API key.*
5. **Done!** Check your Desktop for the new **WriteupForge** icon. Double-click it to start!

---

## 🔄 Updating WriteupForge

WriteupForge is actively maintained. Users can update to the latest version using:

### If you installed with pip:
```bash
pip install --upgrade git+https://github.com/fsociety-pk/writeupforge.git
```

### If you cloned the repository:
```bash
cd writeupforge
git pull origin main
pip install -e .
```

### Check your current version:
```bash
fgwrite --version
```

---

## 📦 Latest Releases

- **v1.2.1** - Fixed writeup structure preservation (preserves raw notes exactly)
- **v1.2.0** - Automatic spell & grammar checking
- **v1.1.0** - Automatic writeup type detection and GitHub-ready output

👉 **[View all releases](https://github.com/fsociety-pk/writeupforge/releases)**

---

## 🎯 What's New in v1.1.0?

### Automatic Writeup Type Detection
WriteupForge now intelligently detects what type of writeup you're creating:
- **CTF Challenges** - Challenge writeups from Capture The Flag competitions
- **Lab/Machine Writeups** - Writeups from platforms like HackTheBox, TryHackMe
- **Learning Notes** - Raw notes from learning videos, courses, or tutorials
- **Research** - Technical research and vulnerability analysis
- **Exploitation** - Exploitation techniques and proof of concepts
- **Tool Guides** - Tool usage guides and documentation

### GitHub-Ready Output
Every writeup now generates a complete, ready-to-push project:
```
output/
└── Your_Project_Name/
    ├── README.md       ✅ GitHub documentation
    ├── writeup.md      ✅ Structured document
    └── writeup.pdf     ✅ PDF format
```

### Automatic Structure Adaptation
Based on the detected type, the AI creates the perfect structure with appropriate sections like:
- Reconnaissance, Enumeration, Exploitation (for labs)
- Challenge Description, Solution (for CTFs)
- Core Concepts, Examples, Takeaways (for learning notes)
- And more tailored to your content!

### Better Formatting
- 📊 Automatic table generation for data comparisons
- 🔧 Proper code block formatting with language tags
- 📸 Smart screenshot and diagram placeholders
- 📝 Professional markdown throughout

---

## 📝 How to Use

### Linux (Terminal Mode)
Just type **`fgwrite`** in any terminal folder. It will ask you a few simple questions:
- **Title** (e.g., "Network Protocols Basics" or "HTB Nmap Writeup")
- **Author** (Your name)
- **Platform** (HackTheBox, TryHackMe, Personal Learning, etc.)
- **Difficulty** (Beginner, Intermediate, etc.)
- **Your Notes** (Paste your rough notes and type `DONE` on an empty line)

The tool will:
1. 🤖 Analyze your notes and detect the writeup type
2. 📋 Structure the content appropriately
3. 🎨 Format everything professionally
4. 📁 Create a folder with `README.md`, `writeup.md`, and `writeup.pdf`
5. ✅ Display the organized output ready to push!

### Windows (Graphic Interface)
Open the app from your Desktop icon. 
You will see a clean, simple window where you can type your Title, Name, select options, and paste your notes. Click the **Generate Professional Report** button and your complete project will be created!

### After Generation
Your project is ready to go to GitHub:
```bash
cd output/Your_Project_Name
git init
git add .
git commit -m "Initial commit: Project writeup"
git push origin main
```

---

## ⚙️ Available Commands

### Check Version
```bash
fgwrite --version
# or
fgwrite -v
```
Shows the installed WriteupForge version.

### Force CLI Mode (Linux/macOS)
```bash
fgwrite --cli
```
Launch in terminal mode even on systems that default to GUI.

### Force GUI Mode
```bash
fgwrite --gui
```
Launch the graphical interface.

### Generate Writeup (Default)
```bash
fgwrite
```
Start the interactive writeup generation process.

---

## 🗑️ How to Uninstall

If you ever want to remove it:

**Linux:** 
Run `sudo bash scripts/uninstall.sh` inside the project folder.

**Windows:** 
Run `scripts\uninstall.bat` from the project folder. This will safely remove the virtual environment, cache files, and the shortcuts it created.

---

## License

This project is licensed under the MIT License.
