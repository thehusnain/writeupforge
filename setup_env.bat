@echo off
echo Creating Virtual Environment (venv)...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment.
    pause
    exit /b %errorlevel%
)

echo Activating Environment...
call venv\Scripts\activate

echo Installing Dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo ------------------------------------------------
    echo Environment setup complete!
    echo To run the app, type:
    echo venv\Scripts\activate ^&^& python main_gui.py
    echo ------------------------------------------------
) else (
    echo Error: Failed to install dependencies.
)
pause
