from fpdf import FPDF


class PDF():
    def __init__(self, name):

        self._pdf =FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self._pdf.set_font('helvetica', 'B', 50)
        self._pdf.cell(0, 0, 'CS50 Shirtificate', align="C")
        # Setting font: helvetica bold 15
        #self._pdf.cell(50, 50, 'Fabian Andres', align="C")
        # Rendering logo:
        self._pdf.image(name="shirtificate.png",x=5, y=30, w=200)

        self._pdf.set_font("helvetica", "B", 30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.set_font_size(30)
        self._pdf.text(x=40, y=90, txt= f"{name} took CS50")




name = input("name:")
pdf = PDF(name)
pdf._pdf.output("shirtificate.pdf")
