import click
import os
import sys
import time
import threading
from ai_handler import AIHandler
from pdf_generator import PDFGenerator
from dotenv import load_dotenv

load_dotenv()


@click.command()
@click.option('--title', prompt='Writeup Title', help='Title of the writeup')
@click.option('--author', prompt='Author Name', help='Author name')
@click.option('--platform', prompt='Platform Name', default='Hackviser', help='Platform (HTB, TryHackMe, etc.)')
@click.option('--difficulty', prompt='Difficulty', type=click.Choice(['Beginner', 'Intermediate', 'Advanced']), help='Challenge difficulty')
def run_cli(title, author, platform, difficulty):
    """Convert raw lab notes into professional writeups."""
    click.clear()
    click.echo(click.style("WriteupForge - Professional Cybersecurity Reports", fg='cyan', bold=True))
    click.echo(f"Title: {title}")
    click.echo(f"Author: {author}")
    click.echo(f"Platform: {platform}")
    click.echo(f"Difficulty: {difficulty}")
    click.echo("-" * 40)

    click.echo("\nEnter your raw notes (type 'DONE' on a new line to finish):")
    raw_notes_lines = []
    while True:
        try:
            line = click.get_text_stream('stdin').readline().strip()
            if line.upper() == 'DONE':
                break
            raw_notes_lines.append(line)
        except EOFError:
            break
    
    raw_notes = "\n".join(raw_notes_lines)

    if not raw_notes:
        click.echo(click.style("Error: No notes provided.", fg='red'))
        return

    print("\n")
    done_event = threading.Event()
    
    def animate_progress():
        base_text = "hold on, ai is generating the report..."
        idx = 0
        while not done_event.is_set():
            chars = list(base_text)
            if chars[idx % len(base_text)].isalpha():
                chars[idx % len(base_text)] = chars[idx % len(base_text)].upper()
            sys.stdout.write(f"\r\033[96m{''.join(chars)}\033[0m")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.08)

    spinner_thread = threading.Thread(target=animate_progress)
    spinner_thread.start()
    
    try:
        ai = AIHandler()
        formatted_content = ai.generate_writeup(title, author, platform, difficulty, raw_notes)
        
        done_event.set()
        spinner_thread.join()
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
        
        os.makedirs("output", exist_ok=True)
        
        md_filename = "output/writeup.md"
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(formatted_content)
        
        pdf_filename = "output/writeup.pdf"
        pdf_gen = PDFGenerator(pdf_filename)
        pdf_gen.generate(formatted_content)
        
        click.echo(click.style("\nSuccess! Reports generated:", fg='green', bold=True))
        click.echo(f"Markdown: {os.path.abspath(md_filename)}")
        click.echo(f"PDF: {os.path.abspath(pdf_filename)}")
        
    except Exception as e:
        done_event.set()
        spinner_thread.join()
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
        click.echo(click.style(f"\nError: {str(e)}", fg='red'))


if __name__ == '__main__':
    run_cli()
