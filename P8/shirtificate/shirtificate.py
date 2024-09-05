from fpdf import FPDF
from PIL import Image

def main():
    pdf = FPDF(orientation = "P",format = "A4")
    pdf.add_page()
    image_path = "shirtificate.png"

    with Image.open(image_path) as img:
        image_width,image_height=img.size
    page_width = pdf.w

    dpi = 96
    img_width = image_width * 25.4 / dpi

    x = (page_width - img_width)/2
    pdf.image(image_path,x=x,y = 70,w = img_width)

    pdf.set_font("helvetica", style = "B", size = 45)
    pdf.cell(190, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

    name = input("what's your name? ")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", size = 25)
    pdf.cell(190, 120, f'{name} took CS50', new_x="LMARGIN", new_y="NEXT", align='C')

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
