#!/usr/bin/env python3
"""
WriteupForge CLI Entry Point
Entry point for the `fgwrite` command.
"""

import sys
import os


def main():
    """Main entry point for the fgwrite CLI command."""
    # Determine the install directory:
    # 1. Check /etc/writeupforge-path (set by install.sh on Linux)
    # 2. Fall back to the directory this file lives in
    install_dir = None

    path_file = "/etc/writeupforge-path"
    if os.path.exists(path_file):
        try:
            with open(path_file, "r") as f:
                candidate = f.read().strip()
            if os.path.isdir(candidate):
                install_dir = candidate
        except Exception:
            pass

    if not install_dir:
        install_dir = os.path.dirname(os.path.abspath(__file__))

    # Ensure project modules are importable from install_dir
    if install_dir not in sys.path:
        sys.path.insert(0, install_dir)

    # Load .env from install_dir, not from cwd
    env_file = os.path.join(install_dir, ".env")
    if os.path.exists(env_file):
        try:
            from dotenv import load_dotenv
            load_dotenv(dotenv_path=env_file)
        except PermissionError:
            print(f"[-] Permission Error: Cannot read .env file at {env_file}")
            print("\nFix this by running:")
            print(f"  sudo chown $(whoami):$(whoami) {env_file}")
            print(f"  sudo chmod 600 {env_file}")
            sys.exit(1)
    else:
        print(f"[!] Warning: No .env file found at {env_file}")
        print("[!] Run 'fgwrite --setup-key' or add GROQ_API_KEY to your environment.")

    # Change to install_dir so relative paths (e.g. output/) resolve correctly
    os.chdir(install_dir)

    try:
        from run import run
        run()
    except PermissionError as e:
        if ".env" in str(e):
            print(f"[-] Permission Error: Cannot access .env file at {env_file}")
            print(f"\nFix this by running:")
            print(f"  sudo chown $(whoami):$(whoami) {env_file}")
            print(f"  sudo chmod 600 {env_file}")
            sys.exit(1)
        else:
            raise
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
