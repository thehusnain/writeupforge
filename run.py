import platform
import sys


def run():
    """Multi-platform entry point. Detects OS and launches GUI (Windows) or CLI (Linux)."""
    os_name = platform.system()
    force_gui = '--gui' in sys.argv
    force_cli = '--cli' in sys.argv

    if force_gui:
        from main_gui import run_gui
        run_gui()
    elif force_cli:
        from main import run_cli
        sys.argv = [arg for arg in sys.argv if arg != '--cli']
        run_cli()
    elif os_name == "Windows":
        from main_gui import run_gui
        run_gui()
    elif os_name == "Linux":
        from main import run_cli
        sys.argv = [sys.argv[0]]
        run_cli()
    else:
        from main import run_cli
        sys.argv = [sys.argv[0]]
        run_cli()


if __name__ == "__main__":
    run()
