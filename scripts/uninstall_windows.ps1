# WriteupForge Uninstaller for Windows
# Author: WriteSec

echo "[!] WriteupForge: Starting Uninstallation..."

# 1. Remove Desktop Shortcut
$DesktopPath = "$HOME\Desktop\WriteupForge.lnk"

if (Test-Path $DesktopPath) {
    echo "[/] Removing Desktop shortcut..."
    Remove-Item $DesktopPath
    echo "[+] Desktop shortcut removed."
} else {
    echo "[-] Desktop shortcut not found."
}

# 2. Remove virtual environment
if (Test-Path "venv") {
    echo "[/] Removing virtual environment (this may take a moment)..."
    Remove-Item -Recurse -Force "venv"
    echo "[+] Virtual environment removed."
} else {
    echo "[-] Virtual environment not found."
}

# 3. Keep project folder for reuse
echo ""
echo "[+] Uninstallation complete!"
echo "[~] Project folder kept (you can delete manually if needed)"
echo ""
pause
