from reportlab.pdfgen import canvas 
from reportlab.pdfbase import pdfmetrics

fileName = 'Factura.pdf'
documentTitle = 'FACTURA' + '001'
title = 'FACTURA' + ' 002'
productoslb = 'Id       Producto                                Importe'
productoslb_co = 'Precio Unitario'
prod_co = '$23320.00'; prod_id ='01'; prod_n ='Lápiz'; prod_c =prod_co; prod_c2 =prod_co
id_compra = ['Número de Factura','001']
date = ['Fecha','03/12/2020']

# ------------- Create document 
pdf = canvas.Canvas(fileName, pagesize=(700,450))
pdf.setFontSize(150)
pdf.setTitle(documentTitle)

pdf.setFont("Courier", 12)
pdf.drawString(450,140,"Subtotal = " + " $  " + prod_co)
pdf.drawString(485,105,"IVA = " + " $ " + " 16.00")
pdf.drawString(470,70,"Total = " + " $ " + " 116.00")

pdf.setFont("Courier-Bold", 25)
pdf.drawString(64,400,"FETCHEST")
pdf.drawCentredString(550, 360, title)

pdf.setFont("Courier-Bold", 11)
pdf.drawCentredString(440,320, productoslb)
pdf.drawCentredString(465,320, productoslb_co)

pdf.setFont("Courier", 11)
pdf.drawCentredString(262,300, prod_id)
pdf.drawCentredString(331,300, prod_n)
pdf.drawCentredString(460,300, prod_c)
pdf.drawCentredString(599,300, prod_c2)
# ------------------- Draw lines
pdf.line(185, 390, 60, 390); pdf.line(250, 340, 650, 340)
pdf.line(200, 340, 50, 340); pdf.line(200, 240, 50, 240)
pdf.line(250, 160, 650, 160); pdf.line(430, 125, 650, 125)
pdf.line(430, 90, 650, 90); pdf.line(430, 55, 650, 55)
#--------------------------------------
text = pdf.beginText(50, 315);text.setFont("Courier", 13)
for line in id_compra:
    text.textLine(line)
pdf.drawText(text)

text2 = pdf.beginText(50, 215);text2.setFont("Courier", 13)
for line in date:
    text2.textLine(line)
pdf.drawText(text2)

pdf.save()