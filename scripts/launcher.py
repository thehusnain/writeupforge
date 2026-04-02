#!/usr/bin/env python3
"""
Universal launcher for WriteupForge
Works on Windows, Linux, and macOS
"""

import sys
import platform
import subprocess
from pathlib import Path


def get_python_executable():
    """Get the Python executable path from virtual environment"""
    if platform.system() == "Windows":
        exe = Path("venv") / "Scripts" / "python.exe"
    else:
        exe = Path("venv") / "bin" / "python"
    
    if not exe.exists():
        print(f"ERROR: Virtual environment not found at {exe}")
        print("Please run: python install.py")
        return None
    
    return str(exe)


def main():
    """Launch WriteupForge"""
    python_exe = get_python_executable()
    if not python_exe:
        return 1
    
    try:
        # Pass all command-line arguments to run.py
        result = subprocess.run(
            [python_exe, "run.py"] + sys.argv[1:],
            cwd=Path(__file__).parent
        )
        return result.returncode
    except KeyboardInterrupt:
        print("\nApplication closed")
        return 0
    except Exception as e:
        print(f"ERROR: Failed to launch application: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
