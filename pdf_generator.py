from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER


class PDFGenerator:
    def __init__(self, filename):
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
                clean_line = line.replace('**', '<b>').replace('__', '<b>').replace('*', '<i>').replace('_', '<i>')
                story.append(Paragraph(clean_line, self.styles['CyberBody']))

        doc.build(story)
