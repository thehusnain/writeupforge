"""Input handling and validation module for WriteupForge.

Provides easy-to-use input methods with validation and helpful prompts.
"""

import click
from typing import Optional


class InputHandler:
    """Handles user input with validation and helpful prompts."""

    PLATFORMS = [
        "HackTheBox",
        "TryHackMe",
        "PortSwigger",
        "PentesterLab",
        "OverTheWire",
        "DVWA",
        "WebGoat",
        "OWASP Juice Shop",
        "Other"
    ]

    DIFFICULTIES = ["Beginner", "Intermediate", "Advanced", "Expert"]

    @staticmethod
    def get_title() -> str:
        """Get writeup title from user with validation."""
        while True:
            title = click.prompt(
                click.style("[*] Writeup Title", fg='cyan', bold=True),
                type=str
            ).strip()

            if len(title) < 3:
                click.echo(click.style("[!] Please enter at least 3 characters", fg='yellow'))
                continue

            if len(title) > 100:
                click.echo(click.style("[!] Title too long (max 100 characters)", fg='yellow'))
                continue

            return title

    @staticmethod
    def get_author() -> str:
        """Get author name from user with validation."""
        while True:
            author = click.prompt(
                click.style("[*] Your Name", fg='cyan', bold=True),
                type=str
            ).strip()

            if len(author) < 2:
                click.echo(click.style("[!] Please enter at least 2 characters", fg='yellow'))
                continue

            if len(author) > 50:
                click.echo(click.style("[!] Name too long (max 50 characters)", fg='yellow'))
                continue

            return author

    @staticmethod
    def get_platform() -> str:
        """Get platform name from user with suggestions."""
        click.echo(click.style("\n[*] Select Platform or enter custom:", fg='cyan', bold=True))

        for i, platform in enumerate(InputHandler.PLATFORMS, 1):
            click.echo(f"   {i}. {platform}")

        while True:
            choice = click.prompt(
                click.style("Enter number or custom name", fg='cyan'),
                type=str
            ).strip()

            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(InputHandler.PLATFORMS):
                    selected = InputHandler.PLATFORMS[idx]
                    if selected == "Other":
                        custom = click.prompt(
                            click.style("Enter custom platform name", fg='cyan'),
                            type=str
                        ).strip()
                        if len(custom) >= 2:
                            return custom
                        continue
                    return selected
                else:
                    click.echo(click.style("[!] Invalid selection", fg='yellow'))
                    continue

            if len(choice) >= 2:
                return choice

            click.echo(click.style("[!] Please enter at least 2 characters", fg='yellow'))

    @staticmethod
    def get_difficulty() -> str:
        """Get difficulty level from user with options."""
        click.echo(click.style("\n[*] Select Difficulty Level:", fg='cyan', bold=True))

        for i, diff in enumerate(InputHandler.DIFFICULTIES, 1):
            click.echo(f"   {i}. {diff}")

        while True:
            choice = click.prompt(
                click.style("Enter number (1-4)", fg='cyan'),
                type=int
            )

            if 1 <= choice <= len(InputHandler.DIFFICULTIES):
                return InputHandler.DIFFICULTIES[choice - 1]

            click.echo(click.style("[!] Please enter a valid number", fg='yellow'))

    @staticmethod
    def get_notes() -> str:
        """Get raw lab notes from user with helpful instructions."""
        click.echo(click.style("\n[*] Enter Your Lab Notes", fg='cyan', bold=True))
        click.echo(click.style(
            "(Type or paste your notes below. Type 'DONE' on a new line when finished)\n",
            fg='yellow'
        ))

        notes_lines = []
        empty_lines = 0

        while True:
            try:
                line = click.get_text_stream('stdin').readline().rstrip('\n')

                if line.upper() == 'DONE':
                    break

                if line == '':
                    empty_lines += 1
                    if empty_lines > 2:
                        click.echo(click.style("[!] Too many empty lines — assuming input is done", fg='yellow'))
                        break
                else:
                    empty_lines = 0

                notes_lines.append(line)

            except (EOFError, KeyboardInterrupt):
                break

        notes = "\n".join(notes_lines).strip()

        if not notes:
            click.echo(click.style("[!] No notes provided!", fg='yellow'))
            return InputHandler.get_notes()

        click.echo(click.style(f"\n[+] Received {len(notes)} characters of notes", fg='green'))
        return notes

    @staticmethod
    def get_all_inputs() -> dict:
        """Get all required inputs from user in sequence."""
        click.echo(click.style("\n" + "=" * 50, fg='cyan'))
        click.echo(click.style("WriteupForge - Professional Report Generator", fg='cyan', bold=True))
        click.echo(click.style("=" * 50 + "\n", fg='cyan'))

        title = InputHandler.get_title()
        author = InputHandler.get_author()
        platform = InputHandler.get_platform()
        difficulty = InputHandler.get_difficulty()
        notes = InputHandler.get_notes()

        click.echo(click.style("\n[+] Input Summary:", fg='green'))
        click.echo(f"  - Title      : {title}")
        click.echo(f"  - Author     : {author}")
        click.echo(f"  - Platform   : {platform}")
        click.echo(f"  - Difficulty : {difficulty}")
        click.echo(f"  - Notes      : {len(notes)} characters")

        return {
            "title": title,
            "author": author,
            "platform": platform,
            "difficulty": difficulty,
            "raw_notes": notes
        }

    @staticmethod
    def confirm(message: str = "Do you want to continue?") -> bool:
        """Ask user for yes/no confirmation."""
        response = click.confirm(click.style(message, fg='cyan'), default=True)
        return response
