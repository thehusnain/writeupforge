import click
import os
import sys
from ai_handler import AIHandler
from pdf_generator import PDFGenerator
from input_handler import InputHandler
from spinner import Spinner
from dotenv import load_dotenv

load_dotenv()


def run_cli():
    """Convert raw lab notes into professional writeups via CLI."""
    try:
        # Get all user inputs with validation
        inputs = InputHandler.get_all_inputs()

        # Extract inputs
        title = inputs["title"]
        author = inputs["author"]
        platform = inputs["platform"]
        difficulty = inputs["difficulty"]
        raw_notes = inputs["raw_notes"]

        # Generate writeup with spinner
        spinner = Spinner("AI is generating the report", style='line')
        spinner.start()

        try:
            ai = AIHandler()
            formatted_content = ai.generate_writeup(
                title, author, platform, difficulty, raw_notes
            )

            spinner.stop(final_char='[+]')

            # Create output directory
            os.makedirs("output", exist_ok=True)

            # Save markdown file
            md_filename = f"output/{title.replace(' ', '_')}_Writeup.md"
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(formatted_content)

            # Generate PDF
            pdf_filename = f"output/{title.replace(' ', '_')}_Writeup.pdf"
            pdf_gen = PDFGenerator(pdf_filename)
            pdf_gen.generate(formatted_content)

            # Success message
            click.echo(click.style("\n" + "=" * 50, fg='green', bold=True))
            click.echo(click.style("[+] Reports Generated Successfully!", fg='green', bold=True))
            click.echo(click.style("=" * 50 + "\n", fg='green', bold=True))

            click.echo(f"[*] Markdown : {os.path.abspath(md_filename)}")
            click.echo(f"[*] PDF      : {os.path.abspath(pdf_filename)}")
            click.echo()

        except Exception as e:
            spinner.stop(final_char='[-]')
            click.echo(click.style(f"\n[-] Error: {str(e)}", fg='red', bold=True))
            sys.exit(1)

    except KeyboardInterrupt:
        click.echo(click.style("\n\n[!] Cancelled by user", fg='yellow'))
        sys.exit(0)
    except Exception as e:
        click.echo(click.style(f"\n[-] Unexpected error: {str(e)}", fg='red'))
        sys.exit(1)


if __name__ == '__main__':
    run_cli()
