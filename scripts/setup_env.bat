@echo off
title WriteupForge Setup
echo ================================================
echo  WriteupForge - Environment Setup
echo ================================================
echo.

echo [1/4] Creating Python virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ERROR: Could not create virtual environment.
    echo Make sure Python 3.8+ is installed and in PATH.
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Upgrading pip...
python -m pip install --upgrade pip --quiet

echo [4/4] Installing dependencies...
pip install -r requirements.txt --quiet

if %errorlevel% equ 0 (
    echo.
    echo ================================================
    echo  Setup complete!
    echo ================================================
    echo.
    echo  NEXT STEP: Add your Groq API key!
    echo  1. Create a file called .env in this folder
    echo  2. Add this line inside it:
    echo     GROQ_API_KEY=your_key_here
    echo  3. Get your free key at: https://console.groq.com/keys
    echo.
    echo  Then double-click launch.bat to run the app!
    echo ================================================
) else (
    echo ERROR: Failed to install dependencies.
)
pause
