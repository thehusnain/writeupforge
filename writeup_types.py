"""Writeup Type Detection and Structured Templates"""

class WriteupTypeDetector:
    """Detect the type of writeup from raw notes."""
    
    WRITEUP_TYPES = {
        'ctf': {
            'keywords': ['flag', 'ctf', 'challenge', 'solve', 'binary', 'crypto', 'reverse', 'pwn'],
            'prompt_suffix': 'This is a CTF writeup. Include challenge description, solution approach, and the final flag.'
        },
        'lab': {
            'keywords': ['machine', 'lab', 'htb', 'tryhackme', 'vulnhub', 'exploit', 'root', 'user.txt'],
            'prompt_suffix': 'This is a lab/machine writeup. Include reconnaissance, enumeration, exploitation, and privilege escalation steps.'
        },
        'learning_notes': {
            'keywords': ['learn', 'notes', 'tutorial', 'concept', 'understand', 'basics', 'intro', 'guide'],
            'prompt_suffix': 'These are learning notes. Create a structured educational writeup with explanations, examples, and key takeaways.'
        },
        'research': {
            'keywords': ['research', 'vulnerability', 'analysis', 'technique', 'methodology', 'deep dive'],
            'prompt_suffix': 'This is a research/technique writeup. Include background, methodology, findings, and implications.'
        },
        'exploitation': {
            'keywords': ['exploit', 'vulnerability', 'rce', 'sql injection', 'xss', 'payload', 'poc'],
            'prompt_suffix': 'This is an exploitation writeup. Include vulnerability details, exploitation technique, and proof of concept.'
        },
        'tool_usage': {
            'keywords': ['tool', 'use', 'how to', 'usage', 'example', 'configuration', 'setup'],
            'prompt_suffix': 'This is a tool usage guide. Include tool overview, installation, configuration, and practical examples.'
        }
    }
    
    @staticmethod
    def detect_type(raw_notes: str) -> tuple[str, str]:
        """
        Detect writeup type from raw notes.
        
        Returns:
            tuple: (type_name, type_suffix_string)
        """
        notes_lower = raw_notes.lower()
        scores = {}
        
        for writeup_type, info in WriteupTypeDetector.WRITEUP_TYPES.items():
            score = sum(1 for keyword in info['keywords'] if keyword in notes_lower)
            scores[writeup_type] = score
        
        # Get the type with highest score, default to 'lab' if tie
        detected_type = max(scores, key=scores.get) if max(scores.values()) > 0 else 'lab'
        suffix = WriteupTypeDetector.WRITEUP_TYPES[detected_type]['prompt_suffix']
        
        return detected_type, suffix


class StructuredPromptBuilder:
    """Build structured prompts based on writeup type."""
    
    TEMPLATES = {
        'ctf': {
            'sections': [
                'Challenge Description',
                'Reconnaissance',
                'Analysis',
                'Solution Approach',
                'Solution Implementation',
                'Flag',
                'Key Learnings'
            ]
        },
        'lab': {
            'sections': [
                'Lab Overview',
                'Lab Setup/Requirements',
                'Reconnaissance',
                'Enumeration',
                'Initial Access/Exploitation',
                'Privilege Escalation',
                'Proof of Exploitation',
                'Key Learnings'
            ]
        },
        'learning_notes': {
            'sections': [
                'Topic Overview',
                'Prerequisites',
                'Core Concepts',
                'Practical Examples',
                'Common Pitfalls',
                'Key Takeaways',
                'Further Resources'
            ]
        },
        'research': {
            'sections': [
                'Introduction',
                'Background',
                'Methodology',
                'Findings',
                'Technical Details',
                'Implications & Impact',
                'Mitigation',
                'Conclusion'
            ]
        },
        'exploitation': {
            'sections': [
                'Vulnerability Overview',
                'Affected Versions/Systems',
                'Vulnerability Details',
                'Exploitation Technique',
                'Proof of Concept',
                'Impact Assessment',
                'Remediation'
            ]
        },
        'tool_usage': {
            'sections': [
                'Tool Overview',
                'Installation',
                'Prerequisites',
                'Configuration',
                'Basic Usage',
                'Practical Examples',
                'Best Practices',
                'Troubleshooting'
            ]
        }
    }
    
    @staticmethod
    def build_prompt(writeup_type: str, title: str, raw_notes: str) -> str:
        """Build a structured prompt based on writeup type."""
        
        prompt = f"""You are formatting raw notes into a professional, structured writeup.

CRITICAL: Only format and organize the EXACT content from the raw notes. Do NOT add new sections or information.

Writeup Type: {writeup_type.upper().replace('_', ' ')}
Title: {title}

INSTRUCTIONS:
1. Keep the EXACT same headings and structure from the raw notes
2. Include ALL content from the raw notes - do not skip or omit anything
3. Fix only typos and spelling errors (teh→the, refrence→reference, etc)
4. Organize content into proper Markdown format:
   - Use ## for main headings from the notes
   - Use ### for subheadings from the notes
   - Format lists with proper bullet points or numbered items
   - Use tables ONLY if the raw notes contain table-structured data
   - Format code blocks with triple backticks
5. Do NOT add sections that are not in the raw notes
6. Do NOT remove any information from the raw notes
7. Do NOT reorganize the structure - keep the same order

RAW NOTES TO FORMAT:
{raw_notes}

Your output should be the same content but professionally formatted in Markdown."""
        
        return prompt


class GitHubReadmeGenerator:
    """Generate GitHub-ready README.md files."""
    
    @staticmethod
    def generate_readme(title: str, writeup_type: str, author: str, description: str = None) -> str:
        """Generate a professional GitHub README.md."""
        
        type_display = writeup_type.upper().replace('_', ' ')
        
        readme = f"""# {title}

> **Type**: {type_display}  
> **Author**: {author}  
> **Last Updated**: [Auto-generated]

{f'> {description}' if description else ''}

## Overview

This writeup documents {title.lower()}. It covers the necessary steps, techniques, and procedures to understand and complete this {'challenge' if 'ctf' in writeup_type else 'lab' if 'lab' in writeup_type else 'topic'}.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Walkthrough](#walkthrough)
- [Key Learnings](#key-learnings)
- [Resources](#resources)

## Prerequisites

{'''- Basic understanding of networking and Linux/Windows systems
- Familiarity with common penetration testing tools
- Access to the lab environment or challenge platform''' if 'lab' in writeup_type or 'ctf' in writeup_type else '- Understanding of the topic basics\n- Required tools/software mentioned in the writeup'}

## Getting Started

1. **Read the Writeup**: Start with the main markdown file to understand the approach
2. **Review Sections**: Go through each section systematically
3. **Learn**: Understand the techniques and methodologies used
4. **Practice**: Try to replicate or adapt the techniques

## Walkthrough

See the main writeup file for the detailed step-by-step walkthrough.

## Key Learnings

This writeup covers important concepts including:

- Technical understanding of the topic
- Practical application of techniques
- Problem-solving approaches
- Best practices

## Resources

- Main Writeup: `writeup.md`
- PDF Version: `writeup.pdf`
- [Home Directory](./)

## License

This writeup is provided as educational material. Please respect the platform's terms of service and use responsibly.

---

**Created**: [Auto-generated]  
**Tool**: [WriteupForge](https://github.com/thehusnain/WriteupForge)
"""
        
        return readme
