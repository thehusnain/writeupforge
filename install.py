#!/usr/bin/env python3
"""
Universal installer for WriteupForge - Works on Windows, Linux, and macOS
This script sets up the Python virtual environment and installs dependencies.
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    """Print a formatted header"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'=' * 50}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{text}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'=' * 50}{Colors.RESET}\n")


def print_step(step_num, total, text):
    """Print a step indicator"""
    print(f"{Colors.CYAN}[{step_num}/{total}]{Colors.RESET} {text}")


def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}[+] {text}{Colors.RESET}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}[-] {text}{Colors.RESET}")


def print_info(text):
    """Print info message"""
    print(f"{Colors.YELLOW}{text}{Colors.RESET}")


def is_windows():
    """Check if running on Windows"""
    return platform.system() == "Windows"


def is_macos():
    """Check if running on macOS"""
    return platform.system() == "Darwin"


def is_linux():
    """Check if running on Linux"""
    return platform.system() == "Linux"


def check_python():
    """Check if Python 3.8+ is available"""
    print_step(1, 4, "Checking Python installation...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_error(f"Python 3.8+ required, but found Python {version.major}.{version.minor}")
        return False
    
    print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def create_venv():
    """Create Python virtual environment"""
    print_step(2, 4, "Creating virtual environment...")
    
    venv_path = Path("venv")
    
    if venv_path.exists():
        print_info("Virtual environment already exists")
        return True
    
    try:
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_path)],
            check=True,
            capture_output=True
        )
        print_success("Virtual environment created")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to create virtual environment: {e}")
        return False


def get_pip_executable():
    """Get the pip executable path"""
    if is_windows():
        return Path("venv") / "Scripts" / "pip.exe"
    else:
        return Path("venv") / "bin" / "pip"


def get_python_executable():
    """Get the Python executable path"""
    if is_windows():
        return Path("venv") / "Scripts" / "python.exe"
    else:
        return Path("venv") / "bin" / "python"


def install_dependencies():
    """Install required dependencies"""
    print_step(3, 4, "Installing dependencies...")
    
    pip_exe = get_pip_executable()
    
    if not pip_exe.exists():
        print_error(f"pip not found at {pip_exe}")
        return False
    
    try:
        # Upgrade pip
        subprocess.run(
            [str(pip_exe), "install", "--upgrade", "pip"],
            check=True,
            capture_output=True
        )
        
        # Install requirements
        subprocess.run(
            [str(pip_exe), "install", "-r", "requirements.txt"],
            check=True,
            capture_output=True
        )
        
        print_success("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        return False


def create_env_file():
    """Create .env template file if it doesn't exist"""
    print_step(4, 4, "Creating configuration...")
    
    env_file = Path(".env")
    
    if env_file.exists():
        print_info(".env file already exists")
        return True
    
    try:
        with open(env_file, "w") as f:
            f.write("# WriteupForge Configuration\n")
            f.write("# Get your free Groq API key at: https://console.groq.com/keys\n")
            f.write("GROQ_API_KEY=your_api_key_here\n")
        
        print_success(".env configuration file created")
        return True
    except Exception as e:
        print_error(f"Failed to create .env file: {e}")
        return False


def print_completion_message():
    """Print completion and next steps"""
    print_header("Installation Complete!")
    
    print(f"{Colors.BOLD}Next Steps:{Colors.RESET}")
    print("")
    print("1. Edit the .env file and add your Groq API key:")
    print(f"   {Colors.YELLOW}https://console.groq.com/keys{Colors.RESET}")
    print("")
    
    if is_windows():
        print("2. Run the application:")
        print(f"   {Colors.YELLOW}launch.bat{Colors.RESET}")
        print("")
        print("3. Or for CLI mode:")
        print(f"   {Colors.YELLOW}venv\\\\Scripts\\\\python run.py --cli{Colors.RESET}")
    else:
        print("2. Activate the virtual environment:")
        print(f"   {Colors.YELLOW}source venv/bin/activate{Colors.RESET}")
        print("")
        print("3. Run the application:")
        print(f"   {Colors.YELLOW}python run.py{Colors.RESET}")
        print("")
        print("4. Or use the GUI:")
        print(f"   {Colors.YELLOW}python run.py --gui{Colors.RESET}")
        print("")
        print("5. Or use the CLI:")
        print(f"   {Colors.YELLOW}python run.py --cli{Colors.RESET}")
    
    print("")
    print(f"{Colors.GREEN}[+] WriteupForge is ready to use!{Colors.RESET}")
    print("")


def main():
    """Main installation flow"""
    try:
        print_header("WriteupForge Installation")
        
        if not check_python():
            return 1
        
        if not create_venv():
            return 1
        
        if not install_dependencies():
            return 1
        
        if not create_env_file():
            return 1
        
        print_completion_message()
        return 0
        
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user")
        return 130
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
