"""
Spell Checking and Grammar Correction Module for WriteupForge
Automatically corrects spelling mistakes and common grammar errors in generated writeups.
"""

import re
from typing import Dict, Tuple


class SpellGrammarChecker:
    """
    Handles spell checking and grammar correction for writeup content.
    Uses pattern-based rules and common mistake detection.
    """
    
    # Common spelling mistakes dictionary
    SPELLING_MISTAKES = {
        'teh': 'the',
        'recieve': 'receive',
        'acheive': 'achieve',
        'occured': 'occurred',
        'seperate': 'separate',
        'wierd': 'weird',
        'neccessary': 'necessary',
        'begining': 'beginning',
        'definately': 'definitely',
        'untill': 'until',
        'wich': 'which',
        'thier': 'their',
        'recieve': 'receive',
        'lenght': 'length',
    }
    
    # Common grammar rules
    GRAMMAR_RULES = {
        r'\ba\s+([aeiou])': r'an \1',  # a -> an before vowels
        r'\ban\s+([^aeiou])': r'a \1',  # an -> a before consonants
        r'\s{2,}': ' ',  # Multiple spaces -> single space
        r'([a-z])\s+([?.!,;:])': r'\1\2',  # Space before punctuation
    }
    
    def __init__(self):
        self.corrections_made = []
    
    def check_spelling(self, text: str) -> str:
        """
        Check and correct common spelling mistakes.
        
        Args:
            text: Input text to check
            
        Returns:
            Text with spelling corrections applied
        """
        corrected = text
        
        for mistake, correction in self.SPELLING_MISTAKES.items():
            # Case-insensitive replacement
            pattern = re.compile(r'\b' + re.escape(mistake) + r'\b', re.IGNORECASE)
            matches = pattern.findall(corrected)
            if matches:
                self.corrections_made.append(f"Spelling: '{mistake}' -> '{correction}'")
            
            corrected = pattern.sub(correction, corrected)
        
        return corrected
    
    def check_grammar(self, text: str) -> str:
        """
        Check and correct common grammar mistakes.
        
        Args:
            text: Input text to check
            
        Returns:
            Text with grammar corrections applied
        """
        corrected = text
        
        for pattern, replacement in self.GRAMMAR_RULES.items():
            matches = re.findall(pattern, corrected, re.IGNORECASE)
            if matches:
                self.corrections_made.append(f"Grammar: Applied rule '{pattern}'")
            
            corrected = re.sub(pattern, replacement, corrected, flags=re.IGNORECASE)
        
        return corrected
    
    def fix_capitalization(self, text: str) -> str:
        """
        Fix common capitalization issues.
        
        Args:
            text: Input text to check
            
        Returns:
            Text with capitalization corrections
        """
        corrected = text
        
        # Capitalize start of sentences
        sentences = re.split(r'([.!?])', text)
        fixed_sentences = []
        
        for i, sentence in enumerate(sentences):
            if sentence and i % 2 == 0:  # Only process actual sentences
                if sentence.strip():
                    # Capitalize first letter after sentence boundaries
                    sentence = re.sub(
                        r'^\s*(\w)',
                        lambda m: m.group(1).upper(),
                        sentence
                    )
                    fixed_sentences.append(sentence)
            else:
                fixed_sentences.append(sentence)
        
        corrected = ''.join(fixed_sentences)
        
        if corrected != text:
            self.corrections_made.append("Capitalization: Fixed sentence beginnings")
        
        return corrected
    
    def check_content(self, text: str) -> Tuple[str, Dict]:
        """
        Perform complete spell and grammar check.
        
        Args:
            text: Content to check
            
        Returns:
            Tuple of (corrected_text, corrections_summary)
        """
        self.corrections_made = []
        
        # Apply all corrections
        corrected = self.check_spelling(text)
        corrected = self.check_grammar(corrected)
        corrected = self.fix_capitalization(corrected)
        
        summary = {
            'total_corrections': len(self.corrections_made),
            'corrections': self.corrections_made,
            'original_length': len(text),
            'corrected_length': len(corrected),
        }
        
        return corrected, summary
    
    def get_correction_report(self) -> str:
        """Get a formatted report of corrections made."""
        if not self.corrections_made:
            return "✓ No corrections needed - text is clean!"
        
        report = f"✓ Applied {len(self.corrections_made)} correction(s):\n"
        for correction in self.corrections_made:
            report += f"  • {correction}\n"
        
        return report
