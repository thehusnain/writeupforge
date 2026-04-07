import platform
import sys
import click
from version import CURRENT_VERSION


def run():
    """Multi-platform entry point. Detects OS and launches GUI or CLI."""
    os_name = platform.system()
    force_gui = '--gui' in sys.argv
    force_cli = '--cli' in sys.argv
    show_version = '--version' in sys.argv or '-v' in sys.argv

    # Show version and exit
    if show_version:
        click.echo(click.style("\n" + "=" * 50, fg='blue', bold=True))
        click.echo(click.style("WriteupForge - Professional Writeup Generator", fg='cyan', bold=True))
        click.echo(click.style("=" * 50, fg='blue', bold=True))
        click.echo(click.style(f"\nVersion: {CURRENT_VERSION}", fg='green', bold=True))
        click.echo("")
        sys.exit(0)

    if force_gui:
        from main_gui import run_gui
        run_gui()
    elif force_cli:
        from main import run_cli
        run_cli()
    elif os_name == "Windows":
        # Default to GUI on Windows
        from main_gui import run_gui
        run_gui()
    else:
        # Default to CLI on Linux/macOS
        from main import run_cli
        run_cli()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        click.echo(click.style("\n[!] Application closed by user.", fg='yellow'))
        sys.exit(0)
    except Exception as e:
        click.echo(click.style(f"\n[-] Error: {str(e)}", fg='red'))
        sys.exit(1)
