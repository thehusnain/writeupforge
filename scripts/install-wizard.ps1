# WriteupForge Windows Setup Wizard
# Run as Administrator in PowerShell:
#   powershell -ExecutionPolicy Bypass -File scripts\install-wizard.ps1

param(
    [switch]$Silent = $false
)

# ── Helpers ───────────────────────────────────────────────────────────────────
function Write-Header {
    param([string]$text)
    Write-Host ""
    Write-Host "=================================================" -ForegroundColor Cyan
    Write-Host "  $text" -ForegroundColor Cyan
    Write-Host "=================================================" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Ok {
    param([string]$text)
    Write-Host "[+] $text" -ForegroundColor Green
}

function Write-Info {
    param([string]$text)
    Write-Host "[*] $text" -ForegroundColor Cyan
}

function Write-Warn {
    param([string]$text)
    Write-Host "[!] $text" -ForegroundColor Yellow
}

function Write-Err {
    param([string]$text)
    Write-Host "[-] $text" -ForegroundColor Red
}

# ── Admin check ───────────────────────────────────────────────────────────────
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator
)
if (-not $isAdmin) {
    Write-Host ""
    Write-Warn "This installer needs to run as Administrator."
    Write-Host ""
    Write-Host "Steps:" -ForegroundColor Cyan
    Write-Host "  1. Right-click PowerShell" -ForegroundColor White
    Write-Host "  2. Select 'Run as Administrator'" -ForegroundColor White
    Write-Host "  3. Navigate to the WriteupForge folder" -ForegroundColor White
    Write-Host "  4. Run: powershell -ExecutionPolicy Bypass -File scripts\install-wizard.ps1" -ForegroundColor White
    Write-Host ""
    exit 1
}

Write-Header "WriteupForge Setup Wizard"

$ProjectDir = Split-Path -Parent $PSScriptRoot

# ── STEP 1: API Key ───────────────────────────────────────────────────────────
Write-Host "[1/4] API Key Configuration" -ForegroundColor Cyan
Write-Host ""
Write-Info "A Groq API key is required to use WriteupForge."
Write-Info "Get a free key at: https://console.groq.com/keys"
Write-Host ""

$envFile = "$ProjectDir\.env"
$existingKey = ""

if (Test-Path $envFile) {
    $envContent = Get-Content $envFile -Raw
    if ($envContent -match "GROQ_API_KEY=(.+)") {
        $existingKey = $Matches[1].Trim()
        if ($existingKey -ne "your_api_key_here" -and $existingKey.Length -gt 10) {
            Write-Ok "Existing API key found in .env"
            $useExisting = Read-Host "    Use existing key? (Y/n)"
            if ($useExisting -eq "" -or $useExisting -eq "Y" -or $useExisting -eq "y") {
                $apiKey = $existingKey
            } else {
                $apiKey = Read-Host "    Paste your Groq API key"
            }
        } else {
            $apiKey = Read-Host "    Paste your Groq API key"
        }
    } else {
        $apiKey = Read-Host "    Paste your Groq API key"
    }
} else {
    $apiKey = Read-Host "    Paste your Groq API key"
}

if ([string]::IsNullOrWhiteSpace($apiKey) -or $apiKey -eq "your_api_key_here") {
    Write-Warn "No API key entered. You can add it later via [*] Settings in the app."
    $apiKey = "your_api_key_here"
} else {
    Write-Ok "API key received."
}

# ── STEP 2: Python check ──────────────────────────────────────────────────────
Write-Host ""
Write-Host "[2/4] Checking Python installation..." -ForegroundColor Cyan
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Err "Python is not installed or not in PATH."
    Write-Host ""
    Write-Host "Download Python from: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "(Check 'Add Python to PATH' during installation)" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}
$pythonVersion = & python --version 2>&1
Write-Ok "$pythonVersion found"

# ── STEP 3: Virtual environment & dependencies ────────────────────────────────
Write-Host ""
Write-Host "[3/4] Setting up Python environment..." -ForegroundColor Cyan
$venvPath = "$ProjectDir\venv"

if (Test-Path $venvPath) {
    Write-Info "Virtual environment already exists — skipping."
} else {
    try {
        & python -m venv $venvPath
        Write-Ok "Virtual environment created"
    } catch {
        Write-Err "Failed to create virtual environment: $($_.Exception.Message)"
        exit 1
    }
}

$activateScript = "$venvPath\Scripts\Activate.ps1"
& $activateScript

Write-Info "Installing dependencies..."
try {
    & python -m pip install --upgrade pip --quiet -q
    & pip install -r "$ProjectDir\requirements.txt" --quiet -q
    Write-Ok "Dependencies installed"
} catch {
    Write-Err "Failed to install dependencies: $($_.Exception.Message)"
    exit 1
}

# ── STEP 4: Config, shortcut, start menu ──────────────────────────────────────
Write-Host ""
Write-Host "[4/4] Creating shortcuts and saving configuration..." -ForegroundColor Cyan

# Save .env
@"
# WriteupForge Configuration
# Get a free API key at: https://console.groq.com/keys
GROQ_API_KEY=$apiKey
"@ | Set-Content $envFile -Encoding utf8
Write-Ok "Configuration saved to .env"

# Convert icon.png -> icon.ico if needed
$iconPng = "$ProjectDir\icon.png"
$iconIco = "$ProjectDir\icon.ico"
if ((Test-Path $iconPng) -and -not (Test-Path $iconIco)) {
    Write-Info "Converting icon.png to icon.ico..."
    try {
        & python -c @"
from PIL import Image
img = Image.open(r'$iconPng')
img.save(r'$iconIco', format='ICO', sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print('[+] icon.ico created')
"@
    } catch {
        Write-Warn "Could not convert icon (non-critical). Shortcut will use default icon."
        $iconIco = $null
    }
} elseif (Test-Path $iconIco) {
    Write-Info "icon.ico already exists — skipping conversion."
}

# Desktop shortcut
try {
    $shell = New-Object -ComObject WScript.Shell
    $desktopPath = [Environment]::GetFolderPath("Desktop")
    $shortcutPath = "$desktopPath\WriteupForge.lnk"

    $shortcut = $shell.CreateShortcut($shortcutPath)
    $shortcut.TargetPath = "$venvPath\Scripts\python.exe"
    $shortcut.Arguments = "`"$ProjectDir\run.py`""
    $shortcut.WorkingDirectory = $ProjectDir
    $shortcut.Description = "WriteupForge - Professional Cybersecurity Report Generator"
    if ($iconIco -and (Test-Path $iconIco)) {
        $shortcut.IconLocation = $iconIco
    }
    $shortcut.Save()
    Write-Ok "Desktop shortcut created"
} catch {
    Write-Warn "Could not create desktop shortcut: $($_.Exception.Message)"
}

# Start Menu shortcut
try {
    $startMenuPath = [Environment]::GetFolderPath("Programs")
    $appFolder = "$startMenuPath\WriteupForge"
    if (-not (Test-Path $appFolder)) {
        New-Item -ItemType Directory -Path $appFolder | Out-Null
    }

    $smShortcut = $shell.CreateShortcut("$appFolder\WriteupForge.lnk")
    $smShortcut.TargetPath = "$venvPath\Scripts\python.exe"
    $smShortcut.Arguments = "`"$ProjectDir\run.py`""
    $smShortcut.WorkingDirectory = $ProjectDir
    $smShortcut.Description = "WriteupForge - Professional Cybersecurity Report Generator"
    if ($iconIco -and (Test-Path $iconIco)) {
        $smShortcut.IconLocation = $iconIco
    }
    $smShortcut.Save()
    Write-Ok "Start Menu shortcut created"
} catch {
    Write-Warn "Could not create Start Menu shortcut: $($_.Exception.Message)"
}

# ── Done ──────────────────────────────────────────────────────────────────────
Write-Header "Installation Complete"

Write-Host "WriteupForge is ready to use." -ForegroundColor Green
Write-Host ""
Write-Host "  - Double-click the WriteupForge icon on your Desktop" -ForegroundColor White
Write-Host "  - Or find it in: Start Menu > WriteupForge" -ForegroundColor White
Write-Host "  - Reports are saved in: $ProjectDir\output" -ForegroundColor White
Write-Host ""

if ($apiKey -eq "your_api_key_here") {
    Write-Warn "Remember to add your API key via [*] Settings inside the app."
    Write-Host "   Get a free key at: https://console.groq.com/keys" -ForegroundColor Cyan
    Write-Host ""
}

$launch = Read-Host "Launch WriteupForge now? (Y/n)"
if ($launch -eq "" -or $launch -eq "Y" -or $launch -eq "y") {
    Write-Info "Starting WriteupForge..."
    & python "$ProjectDir\run.py"
} else {
    Write-Ok "Setup complete. Launch WriteupForge from your Desktop or Start Menu."
}
