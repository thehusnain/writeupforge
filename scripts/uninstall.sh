#!/bin/bash
# WriteupForge - Linux Uninstaller
#
# Usage:
#   sudo bash scripts/uninstall.sh

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ok()   { echo -e "${GREEN}[+]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
err()  { echo -e "${RED}[-]${NC} $1"; }

if [ "$EUID" -ne 0 ]; then
    err "This script needs sudo. Run with:"
    echo "    sudo bash scripts/uninstall.sh"
    exit 1
fi

echo ""
echo "WriteupForge - Uninstaller"
echo "=========================="
echo ""

if [ -f "/usr/local/bin/fgwrite" ]; then
    rm /usr/local/bin/fgwrite
    ok "Removed /usr/local/bin/fgwrite"
else
    warn "/usr/local/bin/fgwrite not found — skipping"
fi

if [ -f "/etc/writeupforge-path" ]; then
    rm /etc/writeupforge-path
    ok "Removed /etc/writeupforge-path"
else
    warn "/etc/writeupforge-path not found — skipping"
fi

echo ""
ok "WriteupForge has been uninstalled."
warn "The project folder and any generated reports were NOT deleted."
warn "Delete the project folder manually if you want a full removal."
echo ""
