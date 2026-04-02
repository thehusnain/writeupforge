#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "================================================"
echo "  WriteupForge - Environment Setup"
echo "================================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}ERROR: Python 3 is not installed.${NC}"
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

echo "[1/4] Creating Python virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: Failed to create virtual environment.${NC}"
    exit 1
fi

echo "[2/4] Activating environment..."
source venv/bin/activate

echo "[3/4] Upgrading pip..."
pip install --upgrade pip --quiet

echo "[4/4] Installing dependencies..."
pip install -r requirements.txt --quiet

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}================================================${NC}"
    echo -e "${GREEN}  Setup complete!${NC}"
    echo -e "${GREEN}================================================${NC}"
    echo ""
    echo -e "${YELLOW}NEXT STEP: Add your Groq API key!${NC}"
    echo "1. Create a file called .env in this folder"
    echo "2. Add this line inside it:"
    echo "   GROQ_API_KEY=your_key_here"
    echo "3. Get your free key at: https://console.groq.com/keys"
    echo ""
    echo -e "${YELLOW}Then run the app with:${NC}"
    echo "source venv/bin/activate && python run.py"
    echo ""
else
    echo -e "${RED}ERROR: Failed to install dependencies.${NC}"
    exit 1
fi
