#!/bin/bash

# WriteupForge Uninstaller for Linux
# Author: WriteSec

echo "[!] WriteupForge: Starting Uninstallation..."

# 1. Remove global command
INSTALL_PATH="/usr/local/bin/fgwrite"

if [ -f "$INSTALL_PATH" ]; then
    echo "[/] Removing global fgwrite command..."
    sudo rm "$INSTALL_PATH"
    if [ $? -eq 0 ]; then
        echo "[+] Global command removed successfully."
    else
        echo "[-] Failed to remove global command. Try with sudo."
    fi
else
    echo "[-] Global command not found at $INSTALL_PATH"
fi

# 2. Remove virtual environment
if [ -d "venv" ]; then
    echo "[/] Removing virtual environment..."
    rm -rf venv
    echo "[+] Virtual environment removed."
else
    echo "[-] Virtual environment not found."
fi

# 3. Keep project folder for reuse
echo ""
echo "[+] Uninstallation complete!"
echo "[~] Project folder kept (you can delete manually if needed)"
echo ""
