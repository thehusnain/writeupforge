# WriteupForge

Convert raw cybersecurity lab notes into professional, structured Markdown and PDF reports.

## Features

- **AI-Powered**: Uses Groq API (super fast, fully supported)
- **Multi-Platform**: CLI for Linux
- **Markdown & PDF Output**: Generated in professional format
- **Easy Setup**: Simple steps for both Windows and Linux users

---

## Prerequisites (All Platforms)

- Python 3.8 or higher
- **Groq API Key** (Get it free at https://console.groq.com/keys)
- Git (optional, for cloning)

---

## ⚠️ CRITICAL SETUP: API KEY (Windows & Linux)

To process your notes, you **must** configure your Groq API key after installing. Failure to do this will result in an error!

1. Go to [Groq Console](https://console.groq.com/keys) and create a free account.
2. Click **Create API Key** and copy the generated key.
3. In your project directory, create a file named exactly `.env`.
4. Inside the `.env` file, add the following line:

```env
GROQ_API_KEY=your_actual_api_key_here
```
*(Make sure to replace the placeholder with the key you copied!)*

---

## Quick Install (pip/pipx)

### Using pip (Recommended)

Install directly from GitHub:
```bash
pip install git+https://github.com/your-username/WriteSec.git
```

Then run:
```bash
writeupforge        # CLI mode
fgwrite            # Shortcut alias for CLI
```

### Using pipx (Isolated Environment)

pipx keeps WriteupForge in an isolated environment (cleaner system):

```bash
pipx install git+https://github.com/your-username/WriteSec.git
```

Then run:
```bash
writeupforge        # CLI mode
fgwrite            # Shortcut alias for CLI
```

---

## Traditional Install (Manual Setup)

If you prefer to run it manually without installing globally:

### [LINUX / KALI] Installation & Setup

**Step 1: Download Project**
```bash
git clone <repository-url>
cd WriteSec
```

**Step 2: Run Setup Script**
```bash
chmod +x setup_env.sh
./setup_env.sh
```

**Step 3: Setup your API Key**
Create the `.env` file as described in the critical setup section above.
```bash
echo "GROQ_API_KEY=gsk_yourkeyhere" > .env
```

**Step 4: Run Application**
Activate the virtual environment and run the CLI interface:
```bash
source venv/bin/activate
python3 run.py
```

### [WINDOWS] Installation & Setup

**Step 1: Download Project**
- Download as ZIP from GitHub and extract, OR
- Open PowerShell and run:
  ```
  git clone <repository-url>
  cd WriteSec
  ```

**Step 2: Setup Python Environment**
- Double-click `setup_env.bat` (it`s in the project folder)
- Wait for the setup to complete

**Step 3: Setup your API Key**
- Right-click in the project folder -> Create New -> Text File
- Rename it to `.env` (note the dot at the start)
- Open `.env` and configure your `GROQ_API_KEY` as described in the critical setup section.

**Step 4: Run Application**
- Open PowerShell in the project folder and run:
  ```powershell
  python run.py
  ```

---

## Output Files

After running the tool and entering your notes, files are saved in the `output/` folder:
- `[Title]_Writeup.md` - Markdown format (ready for git)
- `[Title]_Writeup.pdf` - Professional PDF

---

## License

MIT License - Feel free to use and modify.
