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

CONSTRAINTS:
1. Do NOT add any steps the user did not provide.
2. Do NOT generate fake data, flags, or IP addresses.
3. If notes are missing a section, mark as "Not applicable".
4. Maintain professional, concise, technical tone.
5. Use proper Markdown formatting.
6. Create tables where appropriate for comparisons or data presentation.
7. Use code blocks with proper language specifiers.

FORMATTING GUIDELINES:
- Use H2 (##) for main sections
- Use H3 (###) for subsections
- Code blocks with language: ```language
- Screenshots: [Insert Screenshot: Description]
- Tables when presenting data comparisons

ONLY use provided notes. DO NOT hallucinate."""

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
