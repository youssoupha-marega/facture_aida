from fpdf import FPDF

# Définir le chemin vers ton image
imaga_path = "image.png"  # remplace par ton chemin réel si besoin

# Créer le PDF
pdf = FPDF()
pdf.add_page()

# Ajouter le logo
pdf.image(imaga_path, x=10, y=8, w=40)

# Titre principal
pdf.set_font("Helvetica", size=16, style="B")
pdf.cell(200, 10, txt="InvoiceKODKEE URBAN GETAWAY", ln=True, align="C")
pdf.ln(10)

# Informations de facture
pdf.set_font("Helvetica", size=12)
pdf.cell(100, 10, "Invoice No: 3")
pdf.cell(100, 10, "Date: 08/02/2025", ln=True)
pdf.cell(100, 10, "Terms: NET 0")
pdf.cell(100, 10, "Due Date: 08/02/2025", ln=True)

pdf.ln(10)
pdf.cell(200, 10, "Bill To:", ln=True)
pdf.cell(200, 10, "Papa Issa Diop", ln=True)
pdf.cell(200, 10, "Immeuble Malick Gnaabaly #8", ln=True)
pdf.cell(200, 10, "+221 77 247 46 21", ln=True)

# Détail de la commande
pdf.ln(10)
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(60, 10, "Description")
pdf.cell(40, 10, "Quantity")
pdf.cell(40, 10, "Rate")
pdf.cell(40, 10, "Amount", ln=True)

pdf.set_font("Helvetica", size=12)
pdf.cell(60, 10, "Court Séjour")
pdf.cell(40, 10, "2")
pdf.cell(40, 10, "F CFA 45,000")
pdf.cell(40, 10, "F CFA 90,000", ln=True)

# Totaux
pdf.ln(10)
pdf.cell(200, 10, "Subtotal F CFA 90,000", ln=True)
pdf.cell(200, 10, "TVA 0% F CFA 0", ln=True)
pdf.cell(200, 10, "Total F CFA 90,000", ln=True)
pdf.cell(200, 10, "Paid F CFA 90,000", ln=True)
pdf.cell(200, 10, "BALANCE DUE F CFA 0", ln=True)

# Sauvegarder le fichier
pdf.output("facture_identique.pdf")
