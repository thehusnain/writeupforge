@echo off
REM WriteupForge Uninstaller for Windows
REM Safely removes virtual environment and temporary files

title WriteupForge Uninstallation
echo ================================================
echo  WriteupForge - Uninstallation
echo ================================================
echo.

REM 1. Remove virtual environment
if exist "venv" (
    echo [1/3] Removing virtual environment...
    rmdir /s /q venv
    if %errorlevel% equ 0 (
        echo OK: Virtual environment removed
    ) else (
        echo ERROR: Failed to remove virtual environment
    )
) else (
    echo [1/3] Virtual environment not found
)

REM 2. Remove cache directories
echo [2/3] Removing cache files...
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" rmdir /s /q "%%d"
)
echo OK: Cache files cleaned

REM 3. Remove .pyc files
echo [3/3] Removing Python compiled files...
for /r . %%f in (*.pyc) do (
    if exist "%%f" del "%%f"
)
echo OK: Compiled files removed

echo.
echo ================================================
echo  Uninstallation complete!
echo ================================================
echo.
echo Note: Project folder kept for future use
echo       (delete manually if needed)
echo.
pause
