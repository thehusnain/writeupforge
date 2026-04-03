#!/bin/bash
# WriteupForge - Convenience installer entry point (Linux)
# Delegates to scripts/install-linux.sh
#
# Usage:
#   sudo bash install.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

if [ "$EUID" -ne 0 ]; then
    echo "[-] This installer needs sudo. Run with:"
    echo "    sudo bash install.sh"
    exit 1
fi

exec bash "$SCRIPT_DIR/scripts/install-linux.sh" "$@"
