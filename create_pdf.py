#pip install fpdf
'''
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", style="B", size=16)
pdf.cell(200,10, txt="My first PDF in Python", 1n=True, align="C")

pdf.set_font("Arial", size=12)
pdf.multi_cell(0,10, txt="This is created using Python")

pdf.output("Example.pdf")
print("PDF created successfully!")'''