"""Loading spinner for command-line applications."""

import sys
import time
import threading
from typing import Optional


class Spinner:
    """Terminal spinner for CLI applications."""

    SPINNERS = {
        'dots': {
            'frames': ['|', '/', '-', '\\'],
            'interval': 0.1
        },
        'line': {
            'frames': ['-', '\\', '|', '/'],
            'interval': 0.1
        },
        'arrow': {
            'frames': ['<', '^', '>', 'v'],
            'interval': 0.1
        },
        'box': {
            'frames': ['+', 'x', '+', 'x'],
            'interval': 0.15
        },
        'bounce': {
            'frames': ['.', 'o', 'O', 'o'],
            'interval': 0.1
        },
        'wave': {
            'frames': ['[   ]', '[=  ]', '[== ]', '[===]', '[ ==]', '[  =]', '[   ]'],
            'interval': 0.1
        }
    }

    def __init__(self, message: str = "Loading", style: str = 'line',
                 output_stream=None):
        """Initialize spinner.

        Args:
            message: Text to display with spinner
            style: Spinner style ('dots', 'line', 'arrow', 'box', 'bounce', 'wave')
            output_stream: Stream to write to (default: sys.stdout)
        """
        self.message = message
        self.style = self.SPINNERS.get(style, self.SPINNERS['line'])
        self.output_stream = output_stream or sys.stdout
        self.is_spinning = False
        self.thread = None

    def start(self):
        """Start the spinner."""
        if not self.is_spinning:
            self.is_spinning = True
            self.thread = threading.Thread(target=self._spin, daemon=True)
            self.thread.start()

    def stop(self, final_char: str = '[+]'):
        """Stop the spinner.

        Args:
            final_char: Text to display when stopping
        """
        self.is_spinning = False
        if self.thread:
            self.thread.join()

        self.output_stream.write(f"\r\033[K")
        self.output_stream.write(f"\033[92m{final_char}\033[0m {self.message}\n")
        self.output_stream.flush()

    def update_message(self, new_message: str):
        """Update spinner message."""
        self.message = new_message

    def _spin(self):
        """Internal spin animation."""
        idx = 0
        while self.is_spinning:
            frame = self.style['frames'][idx % len(self.style['frames'])]
            self.output_stream.write(f"\r\033[96m{frame}\033[0m {self.message}")
            self.output_stream.flush()
            time.sleep(self.style['interval'])
            idx += 1


class ProgressSpinner:
    """Spinner for long-running operations with progress indication."""

    def __init__(self, message: str = "Processing"):
        self.message = message
        self.is_running = False
        self.thread = None
        self.current_step = 0
        self.total_steps = 0

    def start(self, total_steps: int = 0):
        """Start progress spinner."""
        if not self.is_running:
            self.is_running = True
            self.total_steps = total_steps
            self.current_step = 0
            self.thread = threading.Thread(target=self._show_progress, daemon=True)
            self.thread.start()

    def update(self, step: Optional[int] = None, message: Optional[str] = None):
        """Update progress."""
        if step is not None:
            self.current_step = step
        if message is not None:
            self.message = message

    def stop(self, message: str = "Complete!"):
        """Stop the spinner."""
        self.is_running = False
        if self.thread:
            self.thread.join()

        sys.stdout.write(f"\r\033[K")
        sys.stdout.write(f"\033[92m[+]\033[0m {message}\n")
        sys.stdout.flush()

    def _show_progress(self):
        """Show animated progress."""
        spinners = ['-', '\\', '|', '/']
        idx = 0

        while self.is_running:
            frame = spinners[idx % len(spinners)]

            if self.total_steps > 0:
                percentage = int((self.current_step / self.total_steps) * 100)
                bar = '#' * (percentage // 5) + '-' * (20 - (percentage // 5))
                sys.stdout.write(f"\r\033[96m{frame}\033[0m {self.message} [{bar}] {percentage}%")
            else:
                sys.stdout.write(f"\r\033[96m{frame}\033[0m {self.message}")

            sys.stdout.flush()
            time.sleep(0.1)
            idx += 1


# Utility functions
def create_spinner(message: str = "Loading", style: str = 'line') -> Spinner:
    """Create and return a new spinner instance."""
    return Spinner(message, style)


def show_loading(message: str = "Processing", duration: int = 2):
    """Show a loading spinner for a specific duration."""
    spinner = Spinner(message, 'line')
    spinner.start()
    time.sleep(duration)
    spinner.stop()
