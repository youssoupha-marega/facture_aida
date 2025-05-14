from fpdf import FPDF

# Nouveau logo fourni
logo_path = "image.png"

# Création du PDF
pdf = FPDF()
pdf.add_page()

# Ajout du logo à gauche (haut-gauche)
pdf.image(logo_path, x=10, y=10, w=40)

# Positionner le texte en bas à gauche du logo
pdf.set_xy(10, 30)  # x aligné au logo, y juste sous le logo (ajustable)
pdf.set_font("Helvetica", size=16, style="B")
pdf.set_text_color(0, 0, 0)  # noir
pdf.cell(100, 10, "KODKEE URBAN GETAWAY", ln=0)

# Position du texte à droite (Invoice bleu)
pdf.set_xy(150, 30)  # position sur la même ligne à droite
pdf.set_font("Helvetica", size=10, style="B")
pdf.set_text_color(0, 102, 204)  # bleu
pdf.cell(40, 10, "Invoice", ln=True, align="R")

# Ligne horizontale sous les deux textes
pdf.set_line_width(0.8)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, 42, 200, 42)




pdf.set_xy(10, 48)
pdf.set_text_color(0, 0, 0)

# Invoice No
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(30, 10, "Invoice No:")  # libellé en gras
pdf.set_font("Helvetica", style="", size=12)
pdf.set_x(60)  # 10 + 50 mm de décalage
pdf.cell(0, 10, "3", ln=True)

# Date
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(30, 10, "Date:")
pdf.set_font("Helvetica", style="", size=12)
pdf.set_x(60)
pdf.cell(0, 10, "08/02/2025", ln=True)

# Terms
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(30, 10, "Terms:")
pdf.set_font("Helvetica", style="", size=12)
pdf.set_x(60)
pdf.cell(0, 10, "NET 0", ln=True)

# Due Date
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(30, 10, "Due Date:")
pdf.set_font("Helvetica", style="", size=12)
pdf.set_x(60)
pdf.cell(0, 10, "08/02/2025", ln=True)



# Ligne horizontale fine (demi-ligne, pas en gras)
pdf.set_line_width(0.2)
pdf.set_draw_color(0, 0, 0)  # noire
pdf.line(10, pdf.get_y() + 5, 105, pdf.get_y() + 5)  # x1, y1, x2, y2


# 🔻 Descendre un petit peu plus pour éviter le chevauchement
pdf.set_y(pdf.get_y() + 8)  # 5 pour la ligne + 3 d'espace visue

# Bill to 
pdf.set_font("Helvetica", style="B", size=12)
pdf.cell(30, 10, "Bill to:")
pdf.set_font("Helvetica", style="", size=12)
pdf.set_x(60)
pdf.cell(0, 10, "Youssoupha Marega", ln=True)

# 🔹 2e ligne : sous le bloc "Invoice No", "Date", etc.
pdf.set_line_width(0.8)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y() + 5, 200, pdf.get_y() + 5)

# 🔻 Ligne verticale à gauche reliant les 3 lignes horizontales
x_vertical = 105  # même que les lignes horizontales
y_top = 42       # haut de la première ligne
y_bottom = pdf.get_y() + 5  # bas de la dernière ligne horizontale

pdf.set_line_width(0.2)
pdf.set_draw_color(0, 0, 0)
pdf.line(x_vertical, y_top, x_vertical, y_bottom)

# Texte plus petit et aligné à droite
pdf.set_font("Helvetica", size=10)  # plus petit
pdf.set_text_color(0, 0, 0)

# 1ère ligne
text1 = "Immeuble Malick Gnaabaly #8"
text1_width = pdf.get_string_width(text1)
pdf.text(x=200 - text1_width, y=50, txt=text1)  # aligné à droite à x=200

# 2e ligne
text2 = "+221 77 247 46 21"
text2_width = pdf.get_string_width(text2)
pdf.text(x=200 - text2_width, y=60, txt=text2)


# 🔹 Ligne fine (0.2) juste après la ligne épaisse
pdf.set_line_width(0.2)
pdf.set_draw_color(0, 0, 0)
pdf.line(10, pdf.get_y() + 16, 200, pdf.get_y() + 20)

Description                  Quantity              Rate                                           Ammont
_____________________________________________________________________________________________________     ligne bien gras 0.8
 Court Séjour                   2           FCFA 15 000                                           FCFA 3000                      

_____________________________________________________________________________________________________     ligne moins gras


                                                                    Subtotal                FCFA 100
                                                                    TVA                     FCFA 152
                                                                    Total                   FCFA 90
                                                                    
                                                                    laiseer ici de l'espace 
                                                                    
                                                                    Paid                    FCFA 10
                                    __________________________________________________________________     ligne bien gras 0.8 Moitie de la page
                                    
                                    
                                                        Balance Due                             FCFA 0







# Sauvegarde
output_path = "tuto.pdf"
pdf.output(output_path)

output_path



