#!/bin/bash

# WriteupForge Uninstaller for Linux/Mac
# Safely removes virtual environment and temporary files

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}WriteupForge: Starting Uninstallation...${NC}"
echo ""

# 1. Remove virtual environment
if [ -d "venv" ]; then
    echo -e "${YELLOW}[1/3]${NC} Removing virtual environment..."
    rm -rf venv
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} Virtual environment removed"
    else
        echo -e "${RED}✗${NC} Failed to remove virtual environment"
    fi
else
    echo -e "${YELLOW}[1/3]${NC} Virtual environment not found"
fi

# 2. Remove cache directories
if [ -d "__pycache__" ]; then
    echo -e "${YELLOW}[2/3]${NC} Removing cache files..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
    echo -e "${GREEN}✓${NC} Cache files removed"
else
    echo -e "${YELLOW}[2/3]${NC} No cache files found"
fi

# 3. Summary
echo ""
echo -e "${GREEN}✓ Uninstallation complete!${NC}"
echo -e "${YELLOW}Note:${NC} Project folder kept for future use (delete manually if needed)"
echo ""
