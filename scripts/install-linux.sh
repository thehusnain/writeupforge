#!/bin/bash

# WriteupForge Linux Installer
# Easy installation for Linux/macOS with pip or pipx

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Helper functions
print_header() {
    echo ""
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}${BOLD}  WriteupForge - Installation Wizard${NC}"
    echo -e "${CYAN}${BOLD}═══════════════════════════════════════════════════════════${NC}"
    echo ""
}

print_step() {
    echo -e "${CYAN}[Step $1/$2]${NC} $3"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_info() {
    echo -e "${YELLOW}ℹ${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Get the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

print_header

# Step 1: Check Python
print_step 1 4 "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed!"
    echo "Please install Python 3.8 or higher:"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  macOS: brew install python3"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
print_success "Python $PYTHON_VERSION found"

# Step 2: Choose installation method
print_step 2 4 "Choosing installation method..."
echo ""
echo -e "${BOLD}Select installation method:${NC}"
echo "  1) ${GREEN}pip${NC} (simplest, recommended)"
echo "  2) ${GREEN}pipx${NC} (isolated environment, cleaner system)"
echo "  3) ${GREEN}Local${NC} (manual venv setup)"
echo ""

read -p "Choose [1-3]: " choice

case $choice in
    1)
        print_step 3 4 "Installing with pip..."
        
        # Check if pip is installed
        if ! command -v pip3 &> /dev/null; then
            print_info "Installing pip..."
            if command -v apt-get &> /dev/null; then
                sudo apt-get update && sudo apt-get install -y python3-pip
            elif command -v dnf &> /dev/null; then
                sudo dnf install -y python3-pip
            elif command -v brew &> /dev/null; then
                brew install python3
            fi
        fi
        
        print_info "Installing WriteupForge globally..."
        pip3 install -e .
        print_success "Installed with pip"
        
        # Configure API key
        print_step 4 4 "Configuring API Key..."
        create_env_file
        ;;
    
    2)
        # Check if pipx is installed
        if ! command -v pipx &> /dev/null; then
            print_info "Installing pipx..."
            pip3 install --user pipx
            
            # Add pipx to PATH
            export PATH="$HOME/.local/bin:$PATH"
            print_success "pipx installed"
        fi
        
        print_step 3 4 "Installing with pipx..."
        pipx install -e .
        print_success "Installed with pipx"
        
        # Configure API key
        print_step 4 4 "Configuring API Key..."
        create_env_file
        ;;
    
    3)
        print_step 3 4 "Setting up local environment..."
        bash scripts/setup_env.sh
        
        # Configure API key
        print_step 4 4 "Configuring API Key..."
        create_env_file
        ;;
    
    *)
        print_error "Invalid choice!"
        exit 1
        ;;
esac

# Function to create .env file in user's config directory
create_env_file() {
    CONFIG_DIR="$HOME/.writeupforge"
    mkdir -p "$CONFIG_DIR"
    
    if [ -f "$CONFIG_DIR/.env" ]; then
        print_info "Config file already exists at $CONFIG_DIR/.env"
        read -p "Do you want to update it? (y/n): " update_env
        if [ "$update_env" != "y" ]; then
            return
        fi
    fi
    
    echo ""
    echo -e "${BOLD}Enter your Groq API Key${NC}"
    echo -e "${YELLOW}(Get free key at: https://console.groq.com/keys)${NC}"
    read -sp "API Key: " api_key
    echo ""
    
    if [ -z "$api_key" ]; then
        print_error "API key cannot be empty. Skipping configuration."
        echo -e "${YELLOW}You can add it later by editing:${NC} ${CYAN}$CONFIG_DIR/.env${NC}"
    else
        echo "GROQ_API_KEY=$api_key" > "$CONFIG_DIR/.env"
        chmod 600 "$CONFIG_DIR/.env"
        print_success "API key saved to $CONFIG_DIR/.env"
    fi
}

# Function to create desktop launcher
create_desktop_launcher() {
    DESKTOP_DIR="$HOME/.local/share/applications"
    mkdir -p "$DESKTOP_DIR"
    
    DESKTOP_FILE="$DESKTOP_DIR/writeupforge.desktop"
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Type=Application
Name=WriteupForge
Comment=Professional Cybersecurity Report Generator
Icon=document-properties
Exec=python3 $SCRIPT_DIR/run.py --gui
Path=$SCRIPT_DIR
Terminal=false
Categories=Utility;Education;Development;
X-AppStream-Ignore=true
EOF
    
    chmod +x "$DESKTOP_FILE"
    print_success "Desktop launcher created"
    
    if command -v update-desktop-database &> /dev/null; then
        update-desktop-database "$DESKTOP_DIR"
    fi
}

# Create .env file in user's config directory
create_env_file() {
    CONFIG_DIR="$HOME/.writeupforge"
    mkdir -p "$CONFIG_DIR"
    
    if [ -f "$CONFIG_DIR/.env" ]; then
        print_info "Config file already exists at $CONFIG_DIR/.env"
        read -p "Do you want to update it? (y/n): " update_env
        if [ "$update_env" != "y" ]; then
            return
        fi
    fi
    
    echo ""
    echo -e "${BOLD}Enter your Groq API Key${NC}"
    echo -e "${YELLOW}(Get free key at: https://console.groq.com/keys)${NC}"
    read -sp "API Key: " api_key
    echo ""
    
    if [ -z "$api_key" ]; then
        print_error "API key cannot be empty. Skipping configuration."
        echo -e "${YELLOW}You can add it later by editing:${NC} ${CYAN}$CONFIG_DIR/.env${NC}"
    else
        echo "GROQ_API_KEY=$api_key" > "$CONFIG_DIR/.env"
        print_success "API key saved to $CONFIG_DIR/.env"
    fi
}

# Configure API key
echo ""
print_step 4 4 "Configuring API Key..."
create_env_file

# Next steps
echo ""
echo -e "${BOLD}📋 Next Steps:${NC}"
echo ""
echo -e "${BOLD}1️⃣  API Key Configuration:${NC}"
if [ -f "$HOME/.writeupforge/.env" ]; then
    echo -e "   ${GREEN}✓ Done!${NC} Your API key is saved in:"
    echo -e "   ${CYAN}$HOME/.writeupforge/.env${NC}"
else
    echo -e "   ${YELLOW}⚠ Skipped!${NC} You can add your API key later:"
    echo -e "   ${CYAN}echo \"GROQ_API_KEY=your_key_here\" > ~/.writeupforge/.env${NC}"
    echo -e "   Get your free key at: ${CYAN}https://console.groq.com/keys${NC}"
fi
echo ""
echo -e "${BOLD}2️⃣  Launch WriteupForge:${NC}"
echo -e "   • Find ${CYAN}WriteupForge${NC} in your applications menu"
echo -e "   • Or run: ${CYAN}writeupforge${NC} or ${CYAN}fgwrite${NC}"
echo ""
echo -e "${BOLD}3️⃣  Start Creating Professional Reports:${NC}"
echo -e "   • Fill in your writeup details"
echo -e "   • Paste your lab notes"
echo -e "   • Click 'Generate Professional Report'"
echo ""
echo -e "${CYAN}📁 Reports saved in: ${SCRIPT_DIR}/output${NC}"
echo -e "${YELLOW}📚 Documentation: ${CYAN}${SCRIPT_DIR#$HOME/}/docs/README.md${NC}"
echo ""
