import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class AIHandler:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
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

        if self.api_key and self.api_key != "your_groq_api_key_here":
            try:
                client = OpenAI(
                    api_key=self.api_key,
                    base_url="https://api.groq.com/openai/v1"
                )
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.2,
                )
                return response.choices[0].message.content
            except Exception as e:
                raise Exception(f"Groq API Error: {str(e)}")

        raise ValueError("GROQ_API_KEY not found in .env file.")
