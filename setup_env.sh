#!/bin/bash
echo "Creating Virtual Environment (venv)..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment."
    exit 1
fi

echo "Activating Environment..."
source venv/bin/activate

echo "Installing Dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "------------------------------------------------"
    echo "Environment setup complete!"
    echo "To run the app, type:"
    echo "source venv/bin/activate && python main_gui.py"
    echo "------------------------------------------------"
else
    echo "Error: Failed to install dependencies."
fi
