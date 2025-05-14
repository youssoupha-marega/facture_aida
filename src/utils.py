from fpdf import FPDF

# Update function to support FCFA properly without splitting it incorrectly

def generate_pdf(
    path_logo,
    nom_entreprise,
    invoice_no,
    date,
    terms,
    due_date,
    bill_to,
    nom_immeuble,
    telephone_immeuble,
    description,
    quantity,
    rate,
    amount,
    subtotal,
    taux_tva,
    tva,
    total,
    paid,
    balance_due,
    output_path
):
    pdf = FPDF()
    pdf.add_page()

    # Logo
    pdf.image(path_logo, x=10, y=10, w=30)

    # Header
    pdf.set_xy(45, 30)  # 10 (x du logo) + 30 (largeur) + 5 (marge)
    pdf.set_font("Helvetica", size=14, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(100, 10, nom_entreprise, ln=0)
    
    
    pdf.set_xy(160, 30)
    pdf.set_font("Helvetica", size=10, style="B")
    pdf.set_text_color(0, 102, 204)
    pdf.cell(40, 10, "Invoice", ln=True, align="R")

    # Horizontal line
    pdf.set_line_width(0.8)
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, 42, 200, 42)

    # Invoice info
    pdf.set_xy(10, 48)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(30, 10, "Invoice No:")
    pdf.set_font("Helvetica", style="", size=12)
    pdf.set_x(60)
    pdf.cell(0, 10, invoice_no, ln=True)

    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(30, 10, "Date:")
    pdf.set_font("Helvetica", style="", size=12)
    pdf.set_x(60)
    pdf.cell(0, 10, date, ln=True)

    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(30, 10, "Terms:")
    pdf.set_font("Helvetica", style="", size=12)
    pdf.set_x(60)
    pdf.cell(0, 10, terms, ln=True)

    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(30, 10, "Due Date:")
    pdf.set_font("Helvetica", style="", size=12)
    pdf.set_x(60)
    pdf.cell(0, 10, due_date, ln=True)

    pdf.set_line_width(0.2)
    pdf.line(10, pdf.get_y() + 5, 105, pdf.get_y() + 5)
    pdf.set_y(pdf.get_y() + 8)

    # Bill to
    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(30, 10, "Bill to:")
    pdf.set_font("Helvetica", style="", size=12)
    pdf.set_x(60)
    pdf.cell(0, 10, bill_to, ln=True)

    # Bottom line
    pdf.set_line_width(0.8)
    pdf.line(10, pdf.get_y() + 5, 200, pdf.get_y() + 5)

    # Vertical separator
    x_vertical = 105
    y_top = 42
    y_bottom = pdf.get_y() + 5
    pdf.set_line_width(0.2)
    pdf.line(x_vertical, y_top, x_vertical, y_bottom)

    # Right-side address
    pdf.set_font("Helvetica", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.text(x=200 - pdf.get_string_width(nom_immeuble), y=50, txt=nom_immeuble)
    pdf.text(x=200 - pdf.get_string_width(telephone_immeuble), y=60, txt=telephone_immeuble)

    pdf.set_line_width(0.2)
    pdf.line(10, pdf.get_y() + 20, 200, pdf.get_y() + 20)
    pdf.set_y(pdf.get_y() + 22)

    # Table headers
    pdf.set_font("Helvetica", style="B", size=12)
    col_widths = [70, 30, 45, 45]
    headers = ["Description", "Quantity", "Rate", "Amount"]
    for i in range(4):
        pdf.cell(col_widths[i], 10, headers[i], border=0)
    pdf.ln()

    # Thick divider
    current_y = pdf.get_y()
    pdf.set_line_width(0.8)
    pdf.line(10, current_y, 200, current_y)
    pdf.set_y(current_y + 2)

    # Table row
    pdf.set_font("Helvetica", style="", size=12)
    row_data = [description, quantity, rate, amount]
    for i in range(4):
        pdf.cell(col_widths[i], 10, row_data[i], border=0)
    pdf.ln()

    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Totals
    pdf.set_font("Helvetica", size=12)
    for label, value in [("Subtotal", subtotal), (f"TVA {taux_tva}", tva), ("Total", total), ("Paid", paid)]:
        pdf.cell(100)
        pdf.cell(50, 10, label, 0, 0, "R")
        pdf.cell(40, 10, value, ln=True, align="R")

    # Final line
    pdf.set_line_width(0.8)
    line_y = pdf.get_y() + 5
    pdf.line(105, line_y, 200, line_y)

    # Balance due
    pdf.set_y(line_y + 2)
    pdf.set_font("Helvetica", style="B", size=12)
    pdf.cell(100)
    pdf.cell(50, 10, "Balance Due", 0, 0, "R")
    pdf.cell(40, 10, balance_due, ln=True, align="R")

    pdf.output(output_path)
    return output_path


#final_invoice_path = generate_pdf(
#    path_logo="logo_aida_living.png",
#    nom_entreprise="Aïda Living - Appartements Meublés à Dakar",
#    invoice_no="3",
#    date="08/02/2025",
#    terms="NET 0",
#    due_date="08/02/2025",
#    bill_to="Youssoupha Marega",
#    nom_immeuble="Immeuble Malick Gnaabaly #8",
#    telephone_immeuble="+221 77 247 46 21",
#    description="Court Séjour",
#    quantity="2",
#    rate="15 000 FCFA",
#    amount="30 000 FCFA",
#    subtotal="100 FCFA",
#    taux_tva = "15%",
#    tva="152 FCFA",
#    total="90 FCFA",
#    paid="10 FCFA",
#    balance_due="0 FCFA",
#    output_path="facture_2000.pdf"
#)

#final_invoice_path

