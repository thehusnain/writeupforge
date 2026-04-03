import os
from groq import Groq
from dotenv import load_dotenv

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
        self.system_prompt = """You are an expert Cybersecurity Technical Writer. Convert raw lab notes into professional, structured writeups for platforms like Hackviser/HTB/TryHackMe.

CONSTRAINTS:
1. Do NOT add any hacking steps the user did not provide.
2. Do NOT generate fake data, flags, or IP addresses.
3. If notes are missing a section, mark as "Not applicable".
4. Maintain professional, concise, technical tone.
5. Use proper Markdown formatting.

REQUIRED SECTIONS:
- Objective
- Lab Setup
- Reconnaissance
- Enumeration
- Exploitation
- Privilege Escalation (if provided)
- Flags/Proof
- What I Learned
- Conclusion

FORMATTING:
- H1 for title, H2 for sections
- Code blocks for commands/output
- Screenshot placeholders: [Insert Screenshot: Description]

ONLY use provided notes. DO NOT hallucinate."""

    def generate_writeup(self, title, author, platform, difficulty, raw_notes):
        user_prompt = f"""Title: {title}
Author: {author}
Platform: {platform}
Difficulty: {difficulty}

RAW NOTES:
{raw_notes}"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.2,
                max_tokens=2048,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Groq API Error: {str(e)}")
