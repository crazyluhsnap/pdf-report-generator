import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def generate_pdf_report(summary_data: dict):
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    os.makedirs("generated_reports", exist_ok=True)

    filepath = os.path.join(
        "generated_reports",
        filename
    )

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=22,
        spaceAfter=20,
    )

    elements = []

    elements.append(
        Paragraph(
            "Student Performance Report",
            title_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Generated on:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            f"<b>Total Students:</b> {summary_data['total_students']}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Subject Statistics",
            styles["Heading1"]
        )
    )

    table_data = [
        ["Subject", "Average", "Highest", "Lowest", "Total"],
        [
            "Math",
            f"{summary_data['average_math']:.2f}",
            summary_data["highest_math"],
            summary_data["lowest_math"],
            summary_data["total_math_marks"],
        ],
        [
            "Science",
            f"{summary_data['average_science']:.2f}",
            summary_data["highest_science"],
            summary_data["lowest_science"],
            summary_data["total_science_marks"],
        ],
        [
            "English",
            f"{summary_data['average_english']:.2f}",
            summary_data["highest_english"],
            summary_data["lowest_english"],
            summary_data["total_english_marks"],
        ],
    ]

    table = Table(table_data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ])
    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "Attendance Statistics",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"""
            <b>Average Attendance:</b> {summary_data['average_attendance']:.2f}%<br/>
            <b>Highest Attendance:</b> {summary_data['highest_attendance']:.2f}%<br/>
            <b>Lowest Attendance:</b> {summary_data['lowest_attendance']:.2f}%
            """,
            styles["Normal"]
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<i>Generated using FastAPI + ReportLab</i>",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return filepath