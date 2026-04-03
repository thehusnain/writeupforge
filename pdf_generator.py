from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
import os
import re


class PDFGenerator:
    def __init__(self, filename):
        # Ensure directory exists for cross-platform compatibility
        os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
        self.filename = filename
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        self.styles.add(ParagraphStyle(
            name='CyberTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=HexColor("#0D47A1"),
            alignment=TA_CENTER,
            spaceAfter=20
        ))
        self.styles.add(ParagraphStyle(
            name='CyberHeading2',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=HexColor("#1A237E"),
            spaceBefore=15,
            spaceAfter=10
        ))
        self.styles.add(ParagraphStyle(
            name='CyberBody',
            parent=self.styles['Normal'],
            fontSize=11,
            leading=14,
            spaceAfter=10
        ))

    def generate(self, content_md):
        doc = SimpleDocTemplate(
            self.filename,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        story = []
        
        lines = content_md.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                story.append(Spacer(1, 6))
                continue

            if line.startswith('# '):
                story.append(Paragraph(line[2:], self.styles['CyberTitle']))
            elif line.startswith('## '):
                story.append(Paragraph(line[3:], self.styles['CyberHeading2']))
            elif line.startswith('### '):
                story.append(Paragraph(line[4:], self.styles['Heading3']))
            elif line.startswith('```'):
                continue
            elif line.startswith('- ') or line.startswith('* '):
                story.append(Paragraph(f"• {line[2:]}", self.styles['CyberBody']))
            elif line.startswith('[Insert Screenshot:'):
                story.append(Spacer(1, 12))
                story.append(Paragraph(f"<i>{line}</i>", self.styles['Italic']))
                story.append(Spacer(1, 12))
            else:
                # Use regex to safely replace bold and italic to ensure balanced tags
                # Bold: **text** or __text__
                clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                clean_line = re.sub(r'__(.*?)__', r'<b>\1</b>', clean_line)
                # Italic: *text* or _text_ (only if surrounded by word boundaries to avoid breaking on snake_case)
                clean_line = re.sub(r'(?<!\w)\*(.*?)\*(?!\w)', r'<i>\1</i>', clean_line)
                clean_line = re.sub(r'(?<!\w)_(.*?)_(?!\w)', r'<i>\1</i>', clean_line)
                
                # Escape any remaining single < or > that might break ReportLab XML parsing
                clean_line = clean_line.replace('<', '&lt;').replace('>', '&gt;')
                # But revert the tags we just intentionally added
                clean_line = clean_line.replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>')
                clean_line = clean_line.replace('&lt;i&gt;', '<i>').replace('&lt;/i&gt;', '</i>')

                try:
                    story.append(Paragraph(clean_line, self.styles['CyberBody']))
                except Exception:
                    # Fallback to plain text if XML parsing still fails
                    story.append(Paragraph(line.replace('<', '&lt;').replace('>', '&gt;'), self.styles['CyberBody']))

        doc.build(story)
