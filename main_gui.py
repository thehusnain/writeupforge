import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import threading
import os
from PIL import Image
from ai_handler import AIHandler
from pdf_generator import PDFGenerator
from update_checker import check_for_updates
from version import CURRENT_VERSION
from dotenv import load_dotenv, set_key

load_dotenv()


class WriteupForgeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("WriteupForge - Professional Cybersecurity Reports")
        self.geometry("950x750")

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

        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="WriteupForge", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.version_label = ctk.CTkLabel(self.sidebar_frame, text=f"v{CURRENT_VERSION}", text_color="gray", font=ctk.CTkFont(size=10))
        self.version_label.grid(row=0, column=0, sticky="s", padx=20, pady=5)
        
        self.new_btn = ctk.CTkButton(self.sidebar_frame, text="New Writeup", command=self.show_writeup_form)
        self.new_btn.grid(row=1, column=0, padx=20, pady=10)
        
        self.settings_btn = ctk.CTkButton(self.sidebar_frame, text="Settings", command=self.show_settings)
        self.settings_btn.grid(row=2, column=0, padx=20, pady=10)
        
        self.update_btn = ctk.CTkButton(self.sidebar_frame, text="Check Updates", command=self.check_updates_click)
        self.update_btn.grid(row=3, column=0, padx=20, pady=10)

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
        
        form_frame = ctk.CTkScrollableFrame(self.main_container, label_text="Create Writeup")
        form_frame.grid(row=0, column=0, sticky="nsew")
        form_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(form_frame, text="Writeup Title:").grid(row=0, column=0, sticky="w", pady=(10, 0))
        self.title_entry = ctk.CTkEntry(form_frame, placeholder_text="e.g., Lame - HackTheBox", width=400)
        self.title_entry.grid(row=1, column=0, sticky="ew", pady=5)

        ctk.CTkLabel(form_frame, text="Author Name:").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.author_entry = ctk.CTkEntry(form_frame, placeholder_text="Your Name", width=400)
        self.author_entry.grid(row=3, column=0, sticky="ew", pady=5)

        ctk.CTkLabel(form_frame, text="Platform:").grid(row=4, column=0, sticky="w", pady=(10, 0))
        self.platform_entry = ctk.CTkEntry(form_frame, placeholder_text="Hackviser")
        self.platform_entry.grid(row=5, column=0, sticky="ew", pady=5)
        self.platform_entry.insert(0, "Hackviser")

        ctk.CTkLabel(form_frame, text="Difficulty Level:").grid(row=6, column=0, sticky="w", pady=(10, 0))
        self.difficulty_choice = ctk.CTkOptionMenu(form_frame, values=["Beginner", "Intermediate", "Advanced"])
        self.difficulty_choice.grid(row=7, column=0, sticky="w", pady=5)

        ctk.CTkLabel(form_frame, text="Raw Lab Notes:").grid(row=8, column=0, sticky="w", pady=(10, 0))
        self.notes_text = ctk.CTkTextbox(form_frame, height=350)
        self.notes_text.grid(row=9, column=0, sticky="ew", pady=5)

        self.gen_btn = ctk.CTkButton(form_frame, text="Generate Writeup", command=self.on_generate_click, height=45, font=ctk.CTkFont(size=14, weight="bold"))
        self.gen_btn.grid(row=10, column=0, pady=25)

        self.progress_bar = ctk.CTkProgressBar(form_frame)
        self.progress_bar.set(0)
        
    def show_settings(self):
        self.clear_container()
        
        settings_frame = ctk.CTkFrame(self.main_container)
        settings_frame.grid(row=0, column=0, sticky="nsew")
        
        ctk.CTkLabel(settings_frame, text="DeepSeek API Settings", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, sticky="w", pady=20, padx=20)
        
        ctk.CTkLabel(settings_frame, text="DeepSeek API Key:", text_color="cyan").grid(row=1, column=0, sticky="w", pady=(10, 0), padx=20)
        self.deepseek_key_entry = ctk.CTkEntry(settings_frame, show="*", width=550)
        self.deepseek_key_entry.grid(row=2, column=0, sticky="w", pady=5, padx=20)
        self.deepseek_key_entry.insert(0, os.getenv("DEEPSEEK_API_KEY", ""))

        info_label = ctk.CTkLabel(settings_frame, text="Get free API key at: https://platform.deepseek.com/", text_color="gray")
        info_label.grid(row=3, column=0, sticky="w", pady=(5, 10), padx=20)

        save_btn = ctk.CTkButton(settings_frame, text="Save Settings", command=self.save_settings)
        save_btn.grid(row=4, column=0, sticky="w", pady=30, padx=20)

    def save_settings(self):
        deepseek_key = self.deepseek_key_entry.get()
        
        set_key(".env", "DEEPSEEK_API_KEY", deepseek_key)
        os.environ["DEEPSEEK_API_KEY"] = deepseek_key
        
        messagebox.showinfo("Success", "API Key saved successfully!")

    def on_generate_click(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        platform = self.platform_entry.get()
        difficulty = self.difficulty_choice.get()
        raw_notes = self.notes_text.get("1.0", tk.END).strip()

        if not all([title, author, raw_notes]):
            messagebox.showerror("Error", "Title, Author, and Notes are required!")
            return

        self.gen_btn.configure(state="disabled", text="Processing...")
        self.progress_bar.grid(row=11, column=0, sticky="ew", pady=10)
        self.progress_bar.start()

        thread = threading.Thread(target=self.process_writeup, args=(title, author, platform, difficulty, raw_notes))
        thread.start()

    def process_writeup(self, title, author, platform, difficulty, raw_notes):
        try:
            ai = AIHandler()
            formatted_content = ai.generate_writeup(title, author, platform, difficulty, raw_notes)
            
            os.makedirs("output", exist_ok=True)
            md_filename = f"output/{title.replace(' ', '_')}_Writeup.md"
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(formatted_content)
            
            pdf_filename = f"output/{title.replace(' ', '_')}_Writeup.pdf"
            pdf_gen = PDFGenerator(pdf_filename)
            pdf_gen.generate(formatted_content)
            
            self.after(0, lambda: self.on_processing_complete(md_filename, pdf_filename))
            
        except Exception as e:
            self.after(0, lambda: self.on_processing_error(str(e)))

    def on_processing_complete(self, md_path, pdf_path):
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.gen_btn.configure(state="normal", text="Generate Writeup")
        
        message = f"Success! Writeup generated.\n\nMD: {os.path.basename(md_path)}\nPDF: {os.path.basename(pdf_path)}\n\nLocation: {os.path.dirname(md_path)}"
        messagebox.showinfo("Success", message)

    def on_processing_error(self, error):
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.gen_btn.configure(state="normal", text="Generate Writeup")
        messagebox.showerror("Error", f"Failed to generate writeup: {error}")

    def auto_check_updates(self):
        """Check for updates on startup (silent if no update available)."""
        has_update, latest_version = check_for_updates()
        if has_update:
            self.after(0, lambda: self.show_update_notification(latest_version))

    def check_updates_click(self):
        """Check for updates when user clicks button."""
        self.update_btn.configure(state="disabled", text="Checking...")
        
        def check():
            has_update, latest_version = check_for_updates()
            self.after(0, lambda: self.update_check_complete(has_update, latest_version))
        
        threading.Thread(target=check, daemon=True).start()

    def update_check_complete(self, has_update, latest_version):
        """Handle update check completion."""
        self.update_btn.configure(state="normal", text="Check Updates")
        
        if latest_version is None:
            messagebox.showwarning("Update Check", "Could not check for updates. Check your internet connection.")
            return
        
        if has_update:
            self.show_update_notification(latest_version)
        else:
            messagebox.showinfo("Update Check", f"You are running the latest version (v{CURRENT_VERSION})!")

    def show_update_notification(self, latest_version):
        """Show notification that update is available."""
        result = messagebox.showinfo(
            "Update Available",
            f"New version available: v{latest_version}\n\n"
            f"Current version: v{CURRENT_VERSION}\n\n"
            f"Visit GitHub to download the latest version.\n"
            f"(Update checking works only on Windows/Linux)"
        )


def run_gui():
    app = WriteupForgeGUI()
    app.mainloop()


if __name__ == "__main__":
    run_gui()
