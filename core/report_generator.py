from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(content, file_path):
    try:
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        c.drawString(100, height - 50, "ChainInspect Smart Contract Audit Report")
        c.drawString(100, height - 100, content)
        c.save()
    except Exception as e:
        raise Exception(f"Failed to generate PDF report: {e}")
