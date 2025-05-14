import streamlit as st
from fpdf import FPDF
from datetime import date

# Titre
st.title("Générateur de Facture")

# Formulaire utilisateur
with st.form("invoice_form"):
    invoice_no = st.text_input("Numéro de facture", "3")
    date_facture = st.date_input("Date de la facture", value=date.today())
    nom_client = st.text_input("Nom du client", "Papa Issa Diop")
    adresse_client = st.text_area("Adresse du client", "Immeuble Malick Gnaabaly #8")
    telephone = st.text_input("Téléphone", "+221 77 247 46 21")
    description = st.text_input("Description", "Court Séjour")
    quantite = st.number_input("Quantité", min_value=1, value=2)
    taux = st.number_input("Tarif (F CFA)", min_value=0, value=45000)
    submit = st.form_submit_button("Générer la facture")

# Génération PDF
if submit:
    montant = quantite * taux

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="InvoiceKODKEE URBAN GETAWAY", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(100, 10, f"Invoice No: {invoice_no}")
    pdf.cell(100, 10, f"Date: {date_facture.strftime('%d/%m/%Y')}", ln=True)

    pdf.cell(100, 10, "Terms: NET 0")
    pdf.cell(100, 10, f"Due Date: {date_facture.strftime('%d/%m/%Y')}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, "Bill To:", ln=True)
    pdf.cell(200, 10, nom_client, ln=True)
    pdf.cell(200, 10, adresse_client, ln=True)
    pdf.cell(200, 10, telephone, ln=True)

    pdf.ln(10)
    pdf.cell(60, 10, "Description")
    pdf.cell(40, 10, "Quantity")
    pdf.cell(40, 10, "Rate")
    pdf.cell(40, 10, "Amount", ln=True)

    pdf.cell(60, 10, description)
    pdf.cell(40, 10, str(quantite))
    pdf.cell(40, 10, f"F CFA {taux:,.0f}")
    pdf.cell(40, 10, f"F CFA {montant:,.0f}", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, f"Subtotal F CFA {montant:,.0f}", ln=True)
    pdf.cell(200, 10, "TVA 0% F CFA 0", ln=True)
    pdf.cell(200, 10, f"Total F CFA {montant:,.0f}", ln=True)
    pdf.cell(200, 10, f"Paid F CFA {montant:,.0f}", ln=True)
    pdf.cell(200, 10, "BALANCE DUE F CFA 0", ln=True)

    # Sauvegarde et affichage
    pdf_path = f"facture_{invoice_no}.pdf"
    pdf.output(pdf_path)

    with open(pdf_path, "rb") as f:
        st.download_button("Télécharger la facture PDF", f, file_name=pdf_path)
