from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from expense_scenarios import expense_projection as exp 
from text_generation import text_gen as gen


def create_pdf(name,  age, retirement_age, life_span, savings, income, liv_exp, health_exp, misc_exp):
    pdf_filename = "static/output_report.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=A4, title=f"Retirement Scenario Report of {name}") 

    # Set up styles for justified text
    styles = getSampleStyleSheet()
    justified_style = styles['BodyText']

    def draw_title(canvas, doc):
        canvas.setFont("Helvetica-Bold", 16) 
        canvas.drawCentredString(A4[0] / 2, A4[1] - 30, f"Retirement Scenario Report of {name}")

    liv_exp_img = 'graphs/living_expenses_plot.png' 
    health_exp_img = 'graphs/health_expenses_plot.png'
    misc_exp_img = 'graphs/misc_expenses_plot.png'
    lng_liv_exp_img = 'graphs/lng_liv_expenses_plot.png'
    lng_health_exp_img = 'graphs/lng_health_expenses_plot.png'
    lng_misc_exp_img = 'graphs/lng_misc_expenses_plot.png' 

    
    content = []
    content.append(Paragraph(f"<b>Introduction</b>", justified_style))
    content.append(Paragraph(f"{gen.section1(name, age, retirement_age, life_span)}", justified_style))

    content.append(Paragraph(f"<b>Savings and Income details</b>", justified_style))
    content.append(Paragraph(f"{gen.section2(name,savings,income)}", justified_style))

    content.append(Paragraph(f"<b>Expense Projections Across Various Scenarios</b>", justified_style))
    content.append(Paragraph(f"<b>Living Expenses </b>", justified_style))
    content.append(Paragraph(f"{gen.section3a(liv_exp)}", justified_style))

    content.append(Image(liv_exp_img, width=400, height=300))
    content.append(Paragraph(f"{exp.exp_text[0]}", justified_style))

    content.append(Paragraph(f"<b>Healthcare Expenses </b>", justified_style))
    content.append(Paragraph(f"{gen.section3b(health_exp)}", justified_style))

    content.append(Image(health_exp_img, width=400, height=300))
    content.append(Paragraph(f"{exp.exp_text[1]}", justified_style))

    content.append(Paragraph(f"<b>Miscellaneous Expenses </b>", justified_style))
    content.append(Paragraph(f"{gen.section3c(name, income, misc_exp)}", justified_style))

    content.append(Image(misc_exp_img, width=400, height=300))
    content.append(Paragraph(f"{exp.exp_text[2]}", justified_style))

    content.append(Paragraph(f"<b>Expense Projection for Extended Life Span Scenario</b>", justified_style))
    content.append(Paragraph(f"{gen.section3d()}", justified_style))

    content.append(Image(lng_liv_exp_img, width=400, height=300))
    content.append(Paragraph(f"{exp.lng_exp_text[0]}", justified_style))

    content.append(Image(lng_health_exp_img, width=400, height=300))
    content.append(Paragraph(f"{exp.lng_exp_text[1]}", justified_style))

    content.append(Image(lng_misc_exp_img, width=400, height=300))
    content.append(Paragraph(f"{exp.lng_exp_text[2]}", justified_style))
 
    # Build the PDF document
    doc.build(content,onFirstPage=draw_title)

    print(f"PDF file '{pdf_filename}' created successfully.")

# exp.expense_projector("John Abraham", 54, 60, 80, 500000,1200000, 300000, 500000, 300000)
# create_pdf("John Abraham", 54, 60, 80, 500000,1200000, 300000, 500000, 300000)
