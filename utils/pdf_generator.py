from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(report_text, output_path):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    content = []

    for line in report_text.split("\n"):

        content.append(
            Paragraph(line, styles["BodyText"])
        )

    doc.build(content)

    return output_path