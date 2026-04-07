# Changelog

All notable changes to WriteupForge will be documented in this file.

## [1.2.0] - April 7, 2026

### ✨ New Features

#### Automatic Spell & Grammar Checking
- New spell checking module automatically corrects common spelling mistakes
- Grammar validation applied to all generated writeups
- Capitalization fixes for proper sentence formatting
- Comprehensive correction reporting to track all changes made

**What Gets Corrected:**
- Common spelling mistakes (teh → the, recieve → receive, etc.)
- Articles usage (a/an before vowels and consonants)
- Multiple spaces normalized to single spaces
- Proper spacing before punctuation marks
- Sentence capitalization

#### Improved Content Quality
- All generated writeups are automatically spell and grammar checked
- Correction summary provided in output
- Maintains original meaning while improving readability
- Ensures professional quality output for GitHub publication

### 🔧 Technical Improvements
- New `spell_grammar_checker.py` module for text correction
- Integrated spell/grammar checking into AI content generation pipeline
- Non-intrusive corrections that preserve technical content integrity

---

## [1.1.0] - April 7, 2026

### ✨ New Features

#### Automatic Writeup Type Detection
- AI now automatically detects the type of writeup from raw notes
- Supports 6 different writeup types:
  - **CTF** - Competitive programming and CTF challenges
  - **Lab** - Machine/Lab writeups (HTB, TryHackMe, VulnHub)
  - **Learning Notes** - Educational content and tutorials
  - **Research** - Technical research and vulnerability analysis
  - **Exploitation** - Exploitation techniques and PoCs
  - **Tool Usage** - Tools guides and usage documentation

#### Adaptive Content Structure
- Content structure adapts based on detected writeup type
- Each type has specifically tailored sections for better organization
- Automatic table generation where appropriate
- Professional formatting with proper code block handling

#### GitHub-Ready Output
- Automatic generation of professional `README.md` files
- README includes:
  - Project overview with metadata
  - Table of contents for easy navigation
  - Prerequisites section tailored to writeup type
  - Getting started guide
  - Key learnings and resources
  - Proper licensing section
- Organized folder structure ready for direct GitHub push

#### Improved Project Organization
- Creates dedicated folders for each writeup project
- Clean file structure:
  ```
  output/
  └── Project_Name/
      ├── README.md      # GitHub-ready documentation
      ├── writeup.md     # Structured writeup
      └── writeup.pdf    # PDF version
  ```

#### Enhanced UI/UX
- Better console output showing detected writeup type
- Clear project structure visualization
- Improved success messages with folder organization information

### 🔧 Technical Improvements

- Increased token limit for better content generation (3000 tokens)
- Improved system prompt for universal writeup handling
- Better markdown formatting guidelines
- Added table support in generated content
- Enhanced code block language specification

### 📚 New Modules

- **writeup_types.py** - Writeup type detection and structured templates
  - `WriteupTypeDetector` - Detects writeup type from content
  - `StructuredPromptBuilder` - Builds type-specific prompts
  - `GitHubReadmeGenerator` - Creates GitHub-ready README files

### 🔄 Updates

- **ai_handler.py**
  - New `detect_writeup_type()` method
  - Enhanced `generate_writeup()` now returns type information
  - New `generate_github_readme()` method

- **main.py**
  - Improved folder structure creation
  - README generation on every writeup
  - Better output formatting and user feedback

- **pyproject.toml**
  - Updated version to 1.1.0
  - Updated description to reflect new features

### 🎯 Benefits

✅ AI adapts to ANY type of writeup, not just labs  
✅ Structured output tailored to content type  
✅ One-command GitHub-ready projects  
✅ Professional README files auto-generated  
✅ No manual organization needed  
✅ Better content structure with tables and formatting  

## [1.0.0] - Initial Release

### Initial Features
- Basic writeup generation from raw notes
- Markdown and PDF output
- CLI interface
- Groq AI integration
- Support for lab-based writeups

---

## 🔄 How to Update to v1.1.0

If you have **WriteupForge v1.0.0** already installed on your system, follow these steps to update:

### For Linux Users

```bash
# 1. Navigate to your WriteupForge installation folder
cd path/to/WriteupForge

# 2. Pull the latest version from GitHub
git pull origin main

# 3. Reinstall with the new updates (optional but recommended)
sudo bash install.sh

# 4. Verify the update
fgwrite --version
```

Or if you want the quick update (without reinstalling):
```bash
cd path/to/WriteupForge
git pull origin main
# That's it! The `fgwrite` command will use the updated code automatically
```

### For Windows Users

```powershell
# 1. Open the WriteupForge folder in File Explorer
# Navigate to your WriteupForge directory

# 2. Open PowerShell in this folder (Shift + Right-click → Open PowerShell here)

# 3. Pull the latest version
git pull origin main

# 4. Reinstall (optional but recommended)
powershell -ExecutionPolicy Bypass -File scripts\install-wizard.ps1

# 5. The app will be updated automatically
```

### What Changes After Update?

**Good news**: Your workflow stays exactly the same!

- ✅ All existing commands work identically
- ✅ Your output folder structure improves (organized by project)
- ✅ Simply enjoy the new features automatically
- ✅ Each writeup now gets a GitHub README automatically

### New Features You'll See

After updating, when you run `fgwrite`:
- AI will detect your writeup type automatically
- Content will be structured specifically for that type
- A professional GitHub README will be created
- Everything organizes in a project folder ready to push

**No configuration needed** — just update and start using!

---

## Notes

For migration from v1.0.0 to v1.1.0:
- Existing workflow remains the same
- Output folder structure will change (now includes project folders)
- README files will be auto-generated alongside writeups
- No breaking changes to CLI commands
- Pull latest code with `git pull origin main`
