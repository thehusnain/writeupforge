# WriteupForge Windows Installer
# Author: WriteSec

echo "[!] WriteupForge: Starting Windows Installation..."

# 1. Setup local environment
.\setup_env.bat

# 2. Create Desktop Shortcut
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$HOME\Desktop\WriteupForge.lnk")
$Shortcut.TargetPath = "$PWD\venv\Scripts\python.exe"
$Shortcut.Arguments = "$PWD\run.py"
$Shortcut.WorkingDirectory = "$PWD"
$Shortcut.IconLocation = "$PWD\icon.png"
$Shortcut.Save()

echo "[+] Success! WriteupForge Desktop Shortcut created."
echo "[~] You can now run WriteupForge directly from your desktop."
pause
