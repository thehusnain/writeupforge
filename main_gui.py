import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import os
from PIL import Image
from ai_handler import AIHandler
from pdf_generator import PDFGenerator
from input_handler import InputHandler
from update_checker import check_for_updates
from version import CURRENT_VERSION
from dotenv import load_dotenv, set_key

load_dotenv()


class WriteupForgeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("WriteupForge - Professional Cybersecurity Reports")
        self.geometry("1000x800")
        self.minsize(800, 600)

        if os.path.exists("icon.png"):
            try:
                self.icon_img = tk.PhotoImage(file="icon.png")
                self.iconphoto(False, self.icon_img)
            except Exception:
                pass

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, text="WriteupForge",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.version_label = ctk.CTkLabel(
            self.sidebar_frame, text=f"v{CURRENT_VERSION}",
            text_color="gray", font=ctk.CTkFont(size=10)
        )
        self.version_label.grid(row=1, column=0, padx=20, pady=5)

        ctk.CTkLabel(self.sidebar_frame, text="", height=10).grid(row=2, column=0)

        self.new_btn = ctk.CTkButton(
            self.sidebar_frame, text="[+] New Writeup",
            command=self.show_writeup_form
        )
        self.new_btn.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.settings_btn = ctk.CTkButton(
            self.sidebar_frame, text="[*] Settings",
            command=self.show_settings
        )
        self.settings_btn.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.update_btn = ctk.CTkButton(
            self.sidebar_frame, text="[~] Check Updates",
            command=self.check_updates_click
        )
        self.update_btn.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        # Main container
        self.main_container = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)

        self.show_writeup_form()

        # Check for updates on startup (in background)
        threading.Thread(target=self.auto_check_updates, daemon=True).start()

    def clear_container(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def show_writeup_form(self):
        self.clear_container()

        form_frame = ctk.CTkScrollableFrame(self.main_container, label_text="[+] Create New Writeup")
        form_frame.grid(row=0, column=0, sticky="nsew")
        form_frame.grid_columnconfigure(0, weight=1)

        # Title
        ctk.CTkLabel(
            form_frame, text="[*] Writeup Title",
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=0, column=0, sticky="w", pady=(15, 5))
        self.title_entry = ctk.CTkEntry(
            form_frame, placeholder_text="e.g., SQL Injection Challenge", height=40
        )
        self.title_entry.grid(row=1, column=0, sticky="ew", pady=5, padx=5)
        ctk.CTkLabel(
            form_frame, text="3-100 characters",
            text_color="gray", font=ctk.CTkFont(size=9)
        ).grid(row=2, column=0, sticky="w", padx=5)

        # Author
        ctk.CTkLabel(
            form_frame, text="[*] Your Name",
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=3, column=0, sticky="w", pady=(15, 5))
        self.author_entry = ctk.CTkEntry(
            form_frame, placeholder_text="Your full name", height=40
        )
        self.author_entry.grid(row=4, column=0, sticky="ew", pady=5, padx=5)
        ctk.CTkLabel(
            form_frame, text="This will appear in the report header",
            text_color="gray", font=ctk.CTkFont(size=9)
        ).grid(row=5, column=0, sticky="w", padx=5)

        # Platform
        ctk.CTkLabel(
            form_frame, text="[*] Platform / CTF",
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=6, column=0, sticky="w", pady=(15, 5))
        self.platform_choice = ctk.CTkOptionMenu(
            form_frame, values=InputHandler.PLATFORMS, height=40
        )
        self.platform_choice.set("HackTheBox")
        self.platform_choice.grid(row=7, column=0, sticky="ew", pady=5, padx=5)
        ctk.CTkLabel(
            form_frame, text="Select from popular platforms or enter custom",
            text_color="gray", font=ctk.CTkFont(size=9)
        ).grid(row=8, column=0, sticky="w", padx=5)

        # Difficulty
        ctk.CTkLabel(
            form_frame, text="[*] Difficulty Level",
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=9, column=0, sticky="w", pady=(15, 5))
        self.difficulty_choice = ctk.CTkOptionMenu(
            form_frame, values=InputHandler.DIFFICULTIES, height=40
        )
        self.difficulty_choice.set("Intermediate")
        self.difficulty_choice.grid(row=10, column=0, sticky="ew", pady=5, padx=5)
        ctk.CTkLabel(
            form_frame, text="Rate the challenge difficulty level",
            text_color="gray", font=ctk.CTkFont(size=9)
        ).grid(row=11, column=0, sticky="w", padx=5)

        # Notes
        ctk.CTkLabel(
            form_frame, text="[*] Lab Notes",
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=12, column=0, sticky="w", pady=(15, 5))
        self.notes_text = ctk.CTkTextbox(form_frame, height=250)
        self.notes_text.grid(row=13, column=0, sticky="ew", pady=5, padx=5)
        self.notes_text.insert(
            "1.0",
            "Paste your raw lab notes here...\n- Step 1: ...\n- Step 2: ...\n- Step 3: ..."
        )
        ctk.CTkLabel(
            form_frame,
            text="Include recon, enumeration, exploitation steps, flags, and lessons learned",
            text_color="gray", font=ctk.CTkFont(size=9)
        ).grid(row=14, column=0, sticky="w", padx=5)

        # Buttons frame
        btn_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        btn_frame.grid(row=15, column=0, sticky="ew", pady=25, padx=5)
        btn_frame.grid_columnconfigure(0, weight=1)

        self.gen_btn = ctk.CTkButton(
            btn_frame,
            text="[+] Generate Professional Report",
            command=self.on_generate_click,
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#2e7d32"
        )
        self.gen_btn.grid(row=0, column=0, sticky="ew")

        self.progress_bar = ctk.CTkProgressBar(form_frame, height=5)
        self.progress_bar.set(0)

    def show_settings(self):
        self.clear_container()

        settings_frame = ctk.CTkScrollableFrame(self.main_container, label_text="[*] API Configuration")
        settings_frame.grid(row=0, column=0, sticky="nsew")
        settings_frame.grid_columnconfigure(0, weight=1)

        info_text = (
            "Configure your Groq API key to enable AI-powered writeup generation.\n\n"
            "Get a free API key at: https://console.groq.com/keys"
        )
        ctk.CTkLabel(
            settings_frame, text=info_text,
            text_color="cyan", wraplength=400
        ).grid(row=0, column=0, sticky="ew", pady=(20, 30), padx=20)

        ctk.CTkLabel(
            settings_frame, text="[*] Groq API Key",
            font=ctk.CTkFont(size=12, weight="bold")
        ).grid(row=1, column=0, sticky="w", pady=(10, 5), padx=20)

        self.groq_key_entry = ctk.CTkEntry(settings_frame, height=40, show="*")
        self.groq_key_entry.grid(row=2, column=0, sticky="ew", pady=5, padx=20)
        self.groq_key_entry.insert(0, os.getenv("GROQ_API_KEY", ""))

        self.groq_key_entry.bind("<Control-v>", self._on_paste_key)

        instructions = (
            "Paste your API key above\n"
            "- The key is masked for security\n"
            "- Click 'Show Key' to verify\n"
            "- Your API key is stored locally in .env"
        )
        ctk.CTkLabel(
            settings_frame, text=instructions,
            text_color="gray", font=ctk.CTkFont(size=9), justify="left"
        ).grid(row=3, column=0, sticky="w", pady=(5, 10), padx=20)

        button_frame = ctk.CTkFrame(settings_frame, fg_color="transparent")
        button_frame.grid(row=4, column=0, sticky="ew", pady=(10, 20), padx=20)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        self.show_key_btn = ctk.CTkButton(
            button_frame, text="[~] Show Key",
            command=self.toggle_show_key,
            height=40, fg_color="gray60"
        )
        self.show_key_btn.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.key_shown = False

        save_btn = ctk.CTkButton(
            button_frame, text="[+] Save API Key",
            command=self.save_settings, height=40
        )
        save_btn.grid(row=0, column=1, sticky="ew")

        test_btn = ctk.CTkButton(
            settings_frame, text="[*] Test Connection",
            command=self.test_api_connection, height=40
        )
        test_btn.grid(row=5, column=0, sticky="ew", pady=10, padx=20)

    def _on_paste_key(self, event=None):
        """Handle paste events for API key entry."""
        try:
            clipboard = self.clipboard_get()
            self.groq_key_entry.delete(0, "end")
            self.groq_key_entry.insert(0, clipboard.strip())
            return "break"
        except Exception as e:
            messagebox.showerror("Paste Error", f"Could not paste: {str(e)}")
            return "break"

    def toggle_show_key(self):
        """Toggle between showing and hiding the API key."""
        if self.key_shown:
            self.groq_key_entry.configure(show="*")
            self.show_key_btn.configure(text="[~] Show Key")
            self.key_shown = False
        else:
            self.groq_key_entry.configure(show="")
            self.show_key_btn.configure(text="[-] Hide Key")
            self.key_shown = True

    def save_settings(self):
        groq_key = self.groq_key_entry.get().strip()

        if not groq_key:
            messagebox.showerror("Error", "Please enter an API key.")
            return

        if len(groq_key) < 10:
            messagebox.showerror("Error", "API key seems too short. Please verify it is correct.")
            return

        set_key(".env", "GROQ_API_KEY", groq_key)
        os.environ["GROQ_API_KEY"] = groq_key

        messagebox.showinfo("Success", "[+] API Key saved successfully!\n\nYou can now generate writeups.")

    def test_api_connection(self):
        """Test the API connection."""
        groq_key = self.groq_key_entry.get().strip()

        if not groq_key:
            messagebox.showerror("Error", "Please enter an API key first.")
            return

        try:
            from groq import Groq
            client = Groq(api_key=groq_key)
            client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": "Say OK only"}],
                max_tokens=5,
            )
            messagebox.showinfo("Success", "[+] API connection successful!\nYour key is valid and working.")
        except Exception as e:
            messagebox.showerror("Connection Failed", f"[-] Error: {str(e)}\n\nPlease check your API key.")

    def on_generate_click(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        platform = self.platform_choice.get()
        difficulty = self.difficulty_choice.get()
        raw_notes = self.notes_text.get("1.0", tk.END).strip()

        if not title:
            messagebox.showerror("Error", "[!] Please enter a writeup title.")
            return

        if len(title) < 3:
            messagebox.showerror("Error", "[!] Title must be at least 3 characters.")
            return

        if not author:
            messagebox.showerror("Error", "[!] Please enter your name.")
            return

        if len(author) < 2:
            messagebox.showerror("Error", "[!] Name must be at least 2 characters.")
            return

        placeholder = "Paste your raw lab notes here...\n- Step 1: ...\n- Step 2: ...\n- Step 3: ..."
        if not raw_notes or raw_notes == placeholder:
            messagebox.showerror("Error", "[!] Please enter your lab notes.")
            return

        self.gen_btn.configure(state="disabled", text="[~] Processing...")
        self.progress_bar.grid(row=16, column=0, sticky="ew", pady=10, padx=5)
        self.progress_bar.set(0)

        thread = threading.Thread(
            target=self.process_writeup,
            args=(title, author, platform, difficulty, raw_notes)
        )
        thread.start()

    def process_writeup(self, title, author, platform, difficulty, raw_notes):
        try:
            self.after(100, lambda: self.progress_bar.set(0.2))
            self.after(100, lambda: self.gen_btn.configure(text="[~] AI Generating..."))

            ai = AIHandler()
            formatted_content = ai.generate_writeup(title, author, platform, difficulty, raw_notes)

            self.after(100, lambda: self.progress_bar.set(0.7))
            self.after(100, lambda: self.gen_btn.configure(text="[~] Creating Files..."))

            os.makedirs("output", exist_ok=True)
            safe_title = title.replace(' ', '_').replace('/', '-')
            md_filename = f"output/{safe_title}_Writeup.md"
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(formatted_content)

            pdf_filename = f"output/{safe_title}_Writeup.pdf"
            pdf_gen = PDFGenerator(pdf_filename)
            pdf_gen.generate(formatted_content)

            self.after(100, lambda: self.progress_bar.set(1.0))
            self.after(100, lambda: self.on_processing_complete(md_filename, pdf_filename))

        except Exception as e:
            self.after(0, lambda: self.on_processing_error(str(e)))

    def on_processing_complete(self, md_path, pdf_path):
        self.progress_bar.grid_forget()
        self.gen_btn.configure(state="normal", text="[+] Generate Professional Report")

        message = (
            f"[+] Your professional writeup has been generated!\n\n"
            f"Markdown : {os.path.basename(md_path)}\n"
            f"PDF      : {os.path.basename(pdf_path)}\n\n"
            f"Location : {os.path.dirname(os.path.abspath(md_path))}"
        )
        messagebox.showinfo("Done", message)

    def on_processing_error(self, error):
        self.progress_bar.grid_forget()
        self.gen_btn.configure(state="normal", text="[+] Generate Professional Report")
        messagebox.showerror(
            "Error",
            f"[-] Failed to generate writeup:\n\n{error}\n\n"
            f"Make sure your API key is configured in Settings."
        )

    def auto_check_updates(self):
        """Check for updates on startup (silent if no update)."""
        has_update, latest_version = check_for_updates()
        if has_update:
            self.after(0, lambda: self.show_update_notification(latest_version))

    def check_updates_click(self):
        """Check for updates when user clicks button."""
        self.update_btn.configure(state="disabled", text="[~] Checking...")

        def check():
            has_update, latest_version = check_for_updates()
            self.after(0, lambda: self.update_check_complete(has_update, latest_version))

        threading.Thread(target=check, daemon=True).start()

    def update_check_complete(self, has_update, latest_version):
        """Handle update check completion."""
        self.update_btn.configure(state="normal", text="[~] Check Updates")

        if latest_version is None:
            messagebox.showwarning(
                "Update Check",
                "[!] Could not check for updates.\n\nPlease check your internet connection."
            )
            return

        if has_update:
            self.show_update_notification(latest_version)
        else:
            messagebox.showinfo("Up to Date", f"[+] You are running the latest version (v{CURRENT_VERSION}).")

    def show_update_notification(self, latest_version):
        """Show notification that an update is available."""
        messagebox.showinfo(
            "Update Available",
            f"[!] New version available: v{latest_version}\n"
            f"Current version: v{CURRENT_VERSION}\n\n"
            f"Visit GitHub to download the latest version."
        )


def run_gui():
    app = WriteupForgeGUI()
    app.mainloop()


if __name__ == "__main__":
    run_gui()
