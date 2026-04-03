# WriteupForge

**WriteupForge** is a tool that takes your rough lab notes and automatically turns them into clear, professional cybersecurity writeups using AI. 

It works on Windows, Linux, and macOS, and generates reports in both **Markdown** and **PDF** formats.

---

## 🛠️ Step 1: Getting Your Free AI API Key

WriteupForge uses Groq's super-fast AI to write the reports. It is completely free!

1. Go to **[console.groq.com/keys](https://console.groq.com/keys)**
2. Click **Create API Key**
3. Copy the key (it starts with `gsk_...`)
4. Save it somewhere safe—you'll need it during installation!

---

## 💻 Step 2: Installation

### For Linux Users

1. Open your terminal.
2. Clone this folder and go into it:
   ```bash
   git clone https://github.com/thehusnain/WriteupForge.git
   cd WriteupForge
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
   cd path\to\WriteupForge
   ```
4. Run the installer:
   ```powershell
   powershell -ExecutionPolicy Bypass -File scripts\install-wizard.ps1
   ```
   *Note: Just like Linux, it will ask for your Groq API key.*
5. **Done!** Check your Desktop for the new **WriteupForge** icon. Double-click it to start!

---

## 📝 How to Use

### Linux (Terminal Mode)
Just type **`fgwrite`** in any terminal folder. It will ask you a few simple questions:
- **Title** (e.g., "Nmap Scan")
- **Author** (Your name)
- **Platform** (HackTheBox, TryHackMe, etc.)
- **Difficulty** (Beginner, Intermediate, etc.)
- **Your Notes** (Paste your rough notes and type `DONE` on an empty line)

The tool will think for a few seconds, and then save the finished `.md` and `.pdf` files inside an `output/` folder wherever you are.

### Windows (Graphic Interface)
Open the app from your Desktop icon. 
You will see a clean, simple window where you can type your Title, Name, select options, and paste your notes. Click the **Generate Professional Report** button and watch the magic happen!

---

## 🗑️ How to Uninstall

If you ever want to remove it:

**Linux:** 
Run `sudo bash scripts/uninstall.sh` inside the project folder.

**Windows:** 
Delete the project folder and the icon from your Desktop.

---

## License

This project is licensed under the MIT License.
