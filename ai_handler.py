import os
from groq import Groq
from dotenv import load_dotenv
from writeup_types import WriteupTypeDetector, StructuredPromptBuilder, GitHubReadmeGenerator
from spell_grammar_checker import SpellGrammarChecker

# Load environment variables with better error handling
try:
    load_dotenv()
except PermissionError as e:
    raise PermissionError(
        f"[!] Permission Error: Cannot read .env file\n"
        f"Error: {str(e)}\n\n"
        f"Fix this by running:\n"
        f"  sudo chown $USER:$USER ~/.writeupforge/.env\n"
        f"  sudo chmod 600 ~/.writeupforge/.env"
    )


class AIHandler:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key or self.api_key == "your_api_key_here":
            raise ValueError(
                "GROQ_API_KEY not found or not set.\n"
                "Please add your API key to the .env file.\n"
                "Get a free key at: https://console.groq.com/keys"
            )

        self.client = Groq(api_key=self.api_key)
        self.system_prompt = """You are an expert Cybersecurity Technical Writer. Convert raw notes into professional, structured writeups.

CRITICAL RULES - MUST FOLLOW:
1. PRESERVE the exact headings and structure from the raw notes - DO NOT create new sections.
2. INCLUDE ALL information from the raw notes - DO NOT skip or omit any words or facts.
3. DO NOT add any content that was not explicitly in the raw notes.
4. DO NOT generate fake data, examples, or information.
5. DO NOT create tables unless the raw notes already contain table-like data.
6. DO NOT add new sections like "Installation", "Configuration", "Troubleshooting" if not in notes.
7. Format ONLY - organize and improve readability, but keep the SAME content and structure.

FORMATTING GUIDELINES:
- Use proper Markdown formatting (bold, italic, lists)
- Use H2 (##) only for top-level headings that exist in the notes
- Use H3 (###) only for subheadings that exist in the notes
- Organize bullet points and lists clearly
- Use tables ONLY if the raw notes contain table-structured data
- Fix typos and spelling errors (teh → the, etc.)
- Keep exact same heading names from the raw notes

YOUR TASK:
Transform the raw notes into cleanly formatted Markdown while:
✅ Keeping all content exactly as provided
✅ Preserving the original structure and headings
✅ Only improving formatting and readability
✅ NOT adding, removing, or changing information

ONLY use provided notes. DO NOT hallucinate or create new content."""

    def detect_writeup_type(self, raw_notes: str) -> tuple[str, str]:
        """
        Detect the type of writeup from raw notes.
        
        Returns:
            tuple: (writeup_type, type_description)
        """
        detected_type, _ = WriteupTypeDetector.detect_type(raw_notes)
        type_descriptions = {
            'ctf': 'CTF Challenge',
            'lab': 'Lab/Machine Writeup',
            'learning_notes': 'Learning Notes & Tutorial',
            'research': 'Research & Analysis',
            'exploitation': 'Exploitation Technique',
            'tool_usage': 'Tool Usage Guide'
        }
        return detected_type, type_descriptions.get(detected_type, 'General Writeup')
    
    def generate_writeup(self, title, author, platform, difficulty, raw_notes):
        """Generate a structured writeup with automatic type detection and spell/grammar checking."""
        
        # Detect writeup type
        writeup_type, type_description = self.detect_writeup_type(raw_notes)
        
        # Build structured prompt
        structured_prompt = StructuredPromptBuilder.build_prompt(writeup_type, title, raw_notes)
        
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": structured_prompt},
                ],
                temperature=0.2,
                max_tokens=3000,  # Increased for better structure
            )
            
            formatted_content = response.choices[0].message.content
            
            # Apply spell and grammar checking
            spell_checker = SpellGrammarChecker()
            formatted_content, corrections = spell_checker.check_content(formatted_content)
            
            return formatted_content, writeup_type, type_description
            
        except Exception as e:
            raise Exception(f"Groq API Error: {str(e)}")
    
    def generate_github_readme(self, title: str, writeup_type: str, author: str, description: str = None) -> str:
        """Generate a GitHub-ready README.md file."""
        return GitHubReadmeGenerator.generate_readme(title, writeup_type, author, description)
