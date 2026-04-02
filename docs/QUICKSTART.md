# WriteupForge - Quick Start Guide

## 🎯 Get Started in 5 Minutes

### Windows Users

1. **Download & Extract**
   - Download as ZIP from GitHub
   - Extract to a folder

2. **Run Setup** (Double-click)
   ```
   setup_env.bat
   ```

3. **Add API Key**
   - Create a file called `.env` (with the dot)
   - Add: `GROQ_API_KEY=your_key_from_console.groq.com`

4. **Launch** (Double-click)
   ```
   launch.bat
   ```

### Linux / macOS Users

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/WriteSec.git
   cd WriteSec
   ```

2. **Run Setup**
   ```bash
   python install.py
   ```

3. **Add API Key**
   ```bash
   echo "GROQ_API_KEY=your_key" > .env
   ```

4. **Launch**
   ```bash
   python run.py
   ```

---

## 🔑 Get Your Free API Key

1. Visit: https://console.groq.com/keys
2. Sign up (takes 2 minutes)
3. Click "Create API Key"
4. Copy the key
5. Add to `.env` file

---

## 📝 Using the App - GUI Mode (Easiest)

### Step-by-Step:

1. **📝 Writeup Title**
   - Enter the name of your challenge
   - Example: "SQL Injection Lab", "Buffer Overflow Practice"
   - Min 3 characters

2. **👤 Your Name**
   - Enter your full name as author
   - This appears in the report header

3. **🎯 Platform / CTF**
   - Select from popular options:
     - HackTheBox
     - TryHackMe
     - PortSwigger
     - PentesterLab
     - Or enter custom platform

4. **⭐ Difficulty Level**
   - Choose: Beginner, Intermediate, Advanced, Expert

5. **📋 Lab Notes**
   - Paste your complete lab notes
   - Include: reconnaissance, enumeration, exploitation
   - Add flags, tools used, lessons learned

6. **Click ✨ Generate Professional Report**
   - Wait for processing to complete
   - Check the `output/` folder

---

## 🖥️ Using the App - CLI Mode (Terminal)

```bash
python run.py --cli
```

Follow the prompts - same easy questions, text interface.

---

## 📂 Find Your Files

After generation, look in:
```
project_folder/output/
├── YourChallengeName_Writeup.md    (Markdown)
└── YourChallengeName_Writeup.pdf   (PDF)
```

Both files are professional, ready to share!

---

## 💡 Tips for Best Results

✅ **Include in notes:**
- What the challenge asked you to do
- Tools you used (nmap, sqlmap, etc.)
- Commands you ran
- Important findings
- Flags or proof of exploitation
- What you learned

❌ **Don't include:**
- Your personal API keys
- Passwords of accounts you used
- Detailed walkthroughs from other sources

---

## ⚙️ Settings - In GUI

Go to **⚙️ Settings** tab to:
- Add or update your Groq API key
- Test your connection with **🔗 Test Connection** button
- Verify everything is working

---

## ❓ Troubleshooting

**"Python not found"**
- Install from https://www.python.org/downloads/
- Make sure to add Python to PATH

**"API Key not found"**
- Go to Settings in the app
- Add your key and save
- Or manually create `.env` file with your key

**"Module not found"**
- Run: `python install.py` again
- Or: `pip install -r requirements.txt`

**"Connection failed"**
- Check internet connection
- Verify API key is correct
- Try **Test Connection** in Settings

---

## 🎉 That's It!

You're all set! Start creating professional cybersecurity writeups now.

**Questions?** See the full [README.md](README.md) for more help.

---

## 📱 Available Commands

```bash
# Default (auto-detects GUI on Windows, CLI on Linux/macOS)
python run.py

# Force GUI mode
python run.py --gui

# Force CLI mode
python run.py --cli
```

---

## 🚀 What Happens Behind the Scenes?

1. You enter your lab notes
2. AI reads and understands your notes
3. AI generates a professional structure
4. Markdown file created (for editing)
5. PDF file created (for sharing)
6. Both saved to `output/` folder

All done in seconds! ⚡


