# WriteupForge Windows Setup Wizard
# This is a user-friendly installer for Windows

param(
    [switch]$Silent = $false
)

# Colors for output
function Write-Header {
    param([string]$text)
    Write-Host ""
    Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║ $text" -ForegroundColor Cyan
    Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Step {
    param([int]$num, [int]$total, [string]$text)
    Write-Host "[$num/$total] $text" -ForegroundColor Green
}

function Write-Info {
    param([string]$text)
    Write-Host "ℹ️  $text" -ForegroundColor Cyan
}

function Write-Error-Custom {
    param([string]$text)
    Write-Host "❌ $text" -ForegroundColor Red
}

function Write-Success {
    param([string]$text)
    Write-Host "✓ $text" -ForegroundColor Green
}

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host ""
    Write-Host "⚠️  WriteupForge Setup Wizard" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "This installer needs to run as Administrator to create shortcuts." -ForegroundColor Yellow
    Write-Host "Please run PowerShell as Administrator and try again." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Steps:" -ForegroundColor Cyan
    Write-Host "1. Right-click on PowerShell" -ForegroundColor White
    Write-Host "2. Select 'Run as Administrator'" -ForegroundColor White
    Write-Host "3. Go to the WriteupForge folder" -ForegroundColor White
    Write-Host "4. Run: powershell -ExecutionPolicy Bypass -File install-wizard.ps1" -ForegroundColor White
    Write-Host ""
    exit 1
}

Write-Header "WriteupForge - Professional Cybersecurity Report Generator"

# Step 1: Check Python
Write-Step 1 4 "Checking Python installation..."
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Error-Custom "Python is not installed or not in PATH!"
    Write-Host ""
    Write-Host "Please download and install Python from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "(Make sure to check 'Add Python to PATH' during installation)" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

# Get Python version
$pythonVersion = & python --version 2>&1
Write-Success "$pythonVersion found"

# Step 2: Create Virtual Environment
Write-Step 2 4 "Setting up Python environment..."
$venvPath = "$PSScriptRoot\venv"

if (Test-Path $venvPath) {
    Write-Info "Virtual environment already exists, skipping..."
} else {
    try {
        & python -m venv $venvPath -ErrorAction Stop
        Write-Success "Virtual environment created"
    } catch {
        Write-Error-Custom "Failed to create virtual environment!"
        Write-Host $_.Exception.Message
        exit 1
    }
}

# Activate venv
$activateScript = "$venvPath\Scripts\Activate.ps1"
& $activateScript

# Step 3: Install Dependencies
Write-Step 3 4 "Installing dependencies..."
try {
    & python -m pip install --upgrade pip --quiet -q
    & pip install -r requirements.txt --quiet -q
    Write-Success "All dependencies installed"
} catch {
    Write-Error-Custom "Failed to install dependencies!"
    Write-Host $_.Exception.Message
    exit 1
}

# Step 4: Create Desktop Shortcut and .env template
Write-Step 4 4 "Creating shortcuts and configuration..."

# Create .env file if it doesn't exist
$envFile = "$PSScriptRoot\.env"
if (-not (Test-Path $envFile)) {
    @"
# WriteupForge Configuration
# Get your free API key at: https://console.groq.com/keys
GROQ_API_KEY=your_api_key_here
"@ | Set-Content $envFile
    Write-Success "Created .env configuration file"
}

# Create Desktop Shortcut
try {
    $shell = New-Object -ComObject WScript.Shell
    $desktopPath = [Environment]::GetFolderPath("Desktop")
    $shortcutPath = "$desktopPath\WriteupForge.lnk"
    
    $shortcut = $shell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = "$venvPath\Scripts\python.exe"
    $shortcut.Arguments = "$PSScriptRoot\run.py"
    $shortcut.WorkingDirectory = $PSScriptRoot
    $shortcut.IconLocation = "$PSScriptRoot\icon.png"
    $shortcut.Description = "WriteupForge - Professional Cybersecurity Report Generator"
    $shortcut.Save()
    
    Write-Success "Desktop shortcut created"
} catch {
    Write-Info "Could not create desktop shortcut (non-critical)"
}

# Create Start Menu folder
try {
    $startMenuPath = [Environment]::GetFolderPath("Programs")
    $appFolderPath = "$startMenuPath\WriteupForge"
    
    if (-not (Test-Path $appFolderPath)) {
        New-Item -ItemType Directory -Path $appFolderPath | Out-Null
    }
    
    $startMenuShortcutPath = "$appFolderPath\WriteupForge.lnk"
    $shell = New-Object -ComObject WScript.Shell
    $shortcut = $shell.CreateShortcut($startMenuShortcutPath)
    $shortcut.TargetPath = "$venvPath\Scripts\python.exe"
    $shortcut.Arguments = "$PSScriptRoot\run.py"
    $shortcut.WorkingDirectory = $PSScriptRoot
    $shortcut.IconLocation = "$PSScriptRoot\icon.png"
    $shortcut.Description = "WriteupForge - Professional Cybersecurity Report Generator"
    $shortcut.Save()
    
    # Create uninstall shortcut
    $uninstallBatPath = "$appFolderPath\Uninstall WriteupForge.lnk"
    $uninstallShortcut = $shell.CreateShortcut($uninstallBatPath)
    $uninstallShortcut.TargetPath = "$PSScriptRoot\uninstall.bat"
    $uninstallShortcut.WorkingDirectory = $PSScriptRoot
    $uninstallShortcut.Description = "Uninstall WriteupForge"
    $uninstallShortcut.Save()
    
    Write-Success "Start Menu shortcuts created"
} catch {
    Write-Info "Could not create Start Menu shortcuts (non-critical)"
}

# Final message
Write-Host ""
Write-Header "Installation Complete! ✨"

Write-Host "📋 Next Steps:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1️⃣  Configure Your API Key:" -ForegroundColor White
Write-Host "   • Open the .env file in the WriteupForge folder" -ForegroundColor White
Write-Host "   • Replace 'your_api_key_here' with your Groq API key" -ForegroundColor White
Write-Host "   • Get a free key at: https://console.groq.com/keys" -ForegroundColor White
Write-Host ""
Write-Host "2️⃣  Launch WriteupForge:" -ForegroundColor White
Write-Host "   • Click the WriteupForge icon on your Desktop" -ForegroundColor White
Write-Host "   • Or find it in Windows Start Menu > WriteupForge" -ForegroundColor White
Write-Host "   • Or run: python run.py" -ForegroundColor White
Write-Host ""
Write-Host "3️⃣  Start Creating:" -ForegroundColor White
Write-Host "   • Fill in your writeup details" -ForegroundColor White
Write-Host "   • Paste your lab notes" -ForegroundColor White
Write-Host "   • Click 'Generate Professional Report'" -ForegroundColor White
Write-Host ""
Write-Host "📁 Your reports will be saved in: $PSScriptRoot\output" -ForegroundColor Cyan
Write-Host ""
Write-Host "❓ Need help? Check out: README.md or QUICKSTART.md" -ForegroundColor Yellow
Write-Host ""

# Ask if user wants to start the app
Write-Host ""
$response = Read-Host "Would you like to launch WriteupForge now? (Y/n)"
if ($response -eq "" -or $response -eq "Y" -or $response -eq "y") {
    Write-Host "Starting WriteupForge..." -ForegroundColor Cyan
    & python run.py
} else {
    Write-Host "Setup complete! You can launch WriteupForge anytime from your Desktop or Start Menu." -ForegroundColor Green
}
