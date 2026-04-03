#!/bin/bash
# WriteupForge - Linux Installer
# Installs WriteupForge system-wide so you can run `fgwrite` from any terminal.
#
# Usage:
#   sudo bash install.sh

set -e

# ── Colors ────────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

print_header() {
    echo ""
    echo -e "${BOLD}${CYAN}=================================================${NC}"
    echo -e "${BOLD}${CYAN}  $1${NC}"
    echo -e "${BOLD}${CYAN}=================================================${NC}"
    echo ""
}

ok()   { echo -e "${GREEN}[+]${NC} $1"; }
info() { echo -e "${CYAN}[*]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
err()  { echo -e "${RED}[-]${NC} $1"; }

# ── Root check ────────────────────────────────────────────────────────────────
if [ "$EUID" -ne 0 ]; then
    err "This installer needs sudo to install system-wide."
    echo ""
    echo "Run with:"
    echo "    sudo bash install.sh"
    echo ""
    exit 1
fi

print_header "WriteupForge - Linux Installation"

# ── Python check ──────────────────────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    err "Python 3 is not installed!"
    echo ""
    echo "Install it first:"
    echo "  Ubuntu/Debian : sudo apt install python3 python3-pip python3-venv"
    echo "  Fedora/RHEL   : sudo dnf install python3 python3-pip"
    echo "  Arch          : sudo pacman -S python python-pip"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
ok "Python $PYTHON_VERSION found"

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

info "Installing from: $PROJECT_DIR"

# ── Virtual environment ───────────────────────────────────────────────────────
echo ""
info "Creating virtual environment..."
cd "$PROJECT_DIR"
python3 -m venv venv
ok "Virtual environment created"

info "Activating virtual environment..."
source venv/bin/activate
ok "Virtual environment activated"

# ── Dependencies ──────────────────────────────────────────────────────────────
echo ""
info "Installing dependencies..."
pip install --upgrade pip setuptools wheel -q
pip install -r requirements.txt -q
ok "Dependencies installed"

# ── Install package (editable) ────────────────────────────────────────────────
echo ""
info "Installing WriteupForge package..."
pip install -e . -q
ok "WriteupForge installed into virtual environment"

# ── Deactivate ────────────────────────────────────────────────────────────────
deactivate

# ── Store install path ────────────────────────────────────────────────────────
echo "$PROJECT_DIR" > /etc/writeupforge-path
ok "Installation path registered at /etc/writeupforge-path"

# ── System-wide wrapper: /usr/local/bin/fgwrite ───────────────────────────────
echo ""
info "Creating system-wide 'fgwrite' command..."

cat > /usr/local/bin/fgwrite << 'WRAPPER_EOF'
#!/bin/bash
# WriteupForge system-wide wrapper
# Reads install path, activates venv, and launches fgwrite from any directory.

if [ -f "/etc/writeupforge-path" ]; then
    INSTALL_DIR=$(cat /etc/writeupforge-path)
else
    echo "[-] WriteupForge installation path not found."
    echo "[!] Please reinstall: sudo bash install.sh"
    exit 1
fi

if [ ! -f "$INSTALL_DIR/venv/bin/activate" ]; then
    echo "[-] Virtual environment not found at: $INSTALL_DIR/venv"
    echo "[!] Please reinstall: sudo bash $INSTALL_DIR/install.sh"
    exit 1
fi

source "$INSTALL_DIR/venv/bin/activate"
cd "$INSTALL_DIR"
exec python3 "$INSTALL_DIR/cli.py" "$@"
WRAPPER_EOF

chmod +x /usr/local/bin/fgwrite
ok "Created /usr/local/bin/fgwrite"

# ── API Key setup ─────────────────────────────────────────────────────────────
echo ""
info "Setting up API configuration..."

ENV_FILE="$PROJECT_DIR/.env"

if [ -f "$ENV_FILE" ]; then
    warn ".env file already exists — skipping API key prompt."
    echo "   To update your key, edit: $ENV_FILE"
else
    echo ""
    echo -e "${BOLD}[*] Groq API Key Required${NC}"
    echo "    Get a free key at: https://console.groq.com/keys"
    echo ""
    read -rsp "    Paste your Groq API key (input hidden): " api_key
    echo ""

    if [ -z "$api_key" ]; then
        warn "No API key provided."
        echo "GROQ_API_KEY=your_api_key_here" > "$ENV_FILE"
        warn "A blank template has been created at: $ENV_FILE"
        warn "Edit it and add your key before using fgwrite."
    else
        echo "GROQ_API_KEY=$api_key" > "$ENV_FILE"

        # Fix ownership so the real user (not root) owns the file
        if [ -n "$SUDO_USER" ]; then
            chown "$SUDO_USER:$SUDO_USER" "$ENV_FILE"
        fi
        chmod 600 "$ENV_FILE"
        ok "API key saved securely to $ENV_FILE"
    fi
fi

# ── Done ──────────────────────────────────────────────────────────────────────
echo ""
print_header "Installation Complete"

echo "You can now use WriteupForge from anywhere:"
echo ""
echo "    fgwrite              (auto-detect mode)"
echo "    fgwrite --cli        (command-line mode)"
echo "    fgwrite --gui        (graphical mode)"
echo ""
ok "Installation directory : $PROJECT_DIR"
ok "Reports saved in       : $PROJECT_DIR/output/"
echo ""
warn "Open a new terminal for the fgwrite command to be available."
echo ""
