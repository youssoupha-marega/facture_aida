import streamlit as st
from datetime import date
from src.utils import generate_pdf  # Ta fonction mise à jour avec taux_tva

st.title("🧾 Générateur de Facture - Youssoupha Marega")

with st.form("invoice_form"):
    path_logo = "logo_aida_living.png"

    nom_entreprise = st.text_input("Nom de l'entreprise", "Aïda Living - Appartements Meublés à Dakar")
    invoice_no = st.text_input("Numéro de facture", "3")
    date_facture = st.date_input("Date", value=date.today())
    terms = st.text_input("Conditions", "NET 0")
    due_date = st.date_input("Date d'échéance", value=date.today())

    bill_to = st.text_input("Facturé à", "Youssoupha Marega")
    nom_immeuble = st.text_input("Nom de l'immeuble", "Immeuble Malick Gnaabaly #8")
    telephone_immeuble = st.text_input("Téléphone", "+221 77 247 46 21")

    description = st.text_input("Description", "Court Séjour")
    quantity = st.text_input("Quantité", "2")
    rate = st.text_input("Prix unitaire (FCFA)", "15 000 FCFA")
    paid = st.text_input("Montant payé (FCFA)", "20 000 FCFA")
    taux_tva_str = st.text_input("Taux de TVA (%)", "0")

    submitted = st.form_submit_button("📄 Générer la facture")

if submitted:
    try:
        # Nettoyage et parsing
        quantity_int = int(quantity)
        rate_int = int(rate.replace("FCFA", "").replace(" ", ""))
        paid_int = int(paid.replace("FCFA", "").replace(" ", ""))
        taux_tva = float(taux_tva_str.replace("%", "").replace(",", ".")) / 100

        # Calculs
        amount_int = quantity_int * rate_int
        subtotal_int = amount_int
        tva_int = int(subtotal_int * taux_tva)
        total_int = subtotal_int + tva_int
        balance_due_int = total_int - paid_int

        # Format FCFA
        format_fcfa = lambda x: f"{x:,.0f} FCFA".replace(",", " ")
        amount = format_fcfa(amount_int)
        subtotal = format_fcfa(subtotal_int)
        tva = format_fcfa(tva_int)
        total = format_fcfa(total_int)
        balance_due = format_fcfa(balance_due_int)
        paid_formatted = format_fcfa(paid_int)

        # Générer PDF
        pdf_path = generate_pdf(
            path_logo=path_logo,
            nom_entreprise=nom_entreprise,
            invoice_no=invoice_no,
            date=str(date_facture),
            terms=terms,
            due_date=str(due_date),
            bill_to=bill_to,
            nom_immeuble=nom_immeuble,
            telephone_immeuble=telephone_immeuble,
            description=description,
            quantity=quantity,
            rate=format_fcfa(rate_int),
            amount=amount,
            subtotal=subtotal,
            taux_tva=f"{float(taux_tva_str):.0f}%",  # Exemple : "18%"
            tva=tva,
            total=total,
            paid=paid_formatted,
            balance_due=balance_due,
            output_path="tuto.pdf"
        )

        with open(pdf_path, "rb") as f:
            st.success("✅ Facture générée avec succès.")
            st.download_button("📥 Télécharger la facture", data=f, file_name="facture.pdf", mime="application/pdf")

    except Exception as e:
        st.error(f"❌ Erreur : {e}")
