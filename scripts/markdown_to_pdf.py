from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap

in_md = 'PROJECT_REPORT.md'
out_pdf = 'PROJECT_REPORT.pdf'

with open(in_md, 'r', encoding='utf-8') as f:
    md = f.read()

# Very simple markdown -> plain text converter (keeps headings and paragraphs)
lines = md.splitlines()
plain = []
for line in lines:
    if line.startswith('#'):
        # heading
        heading = line.lstrip('#').strip()
        plain.append(heading.upper())
        plain.append('')
    else:
        plain.append(line)

text = '\n'.join(plain)

c = canvas.Canvas(out_pdf, pagesize=A4)
width, height = A4
margin = 50
max_width = width - margin*2

wrapped = []
for para in text.split('\n\n'):
    # wrap each paragraph
    para = para.replace('\n', ' ').strip()
    if not para:
        wrapped.append('')
        continue
    wrapped += textwrap.wrap(para, 100)
    wrapped.append('')

y = height - margin
c.setFont('Helvetica-Bold', 14)

for line in wrapped:
    if y < margin + 40:
        c.showPage()
        c.setFont('Helvetica', 11)
        y = height - margin
    if line == '':
        y -= 8
        continue
    # simple heading detection (all uppercase lines from conversion)
    if line.strip() == line.strip().upper() and len(line.strip()) < 80:
        c.setFont('Helvetica-Bold', 12)
        c.drawString(margin, y, line)
        c.setFont('Helvetica', 11)
        y -= 18
    else:
        c.drawString(margin, y, line)
        y -= 14

c.save()
print('Wrote', out_pdf)
