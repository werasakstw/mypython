
# pip install pypdf2
from PyPDF2 import PdfFileReader, PdfFileWriter

def pdf_info():
    with open('data/sample.pdf', 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        print('Author:', info.author)
        print('Creator:', info.creator)
        print('Producer:', info.producer)
        print('Subject:', info.subject)
        print('Title:', info.title)
        print('NumPages:', pdf.getNumPages())
##pdf_info()   

def pdf_copy():
    pdf = PdfFileReader('data/sample.pdf')
    wr = PdfFileWriter()

##    p0 = pdf.getPage(0)     # The first page.
    
    # Rotate:
##    p0 = pdf.getPage(0).rotateClockwise(90)
##    p0 = pdf.getPage(0).rotateCounterClockwise(90)
    
    wr.addPage(p0)
    with open('data/tmp.pdf', 'wb') as f:
        wr.write(f)
##pdf_copy()

def pdf_split():
    pdf = PdfFileReader('data/sample.pdf')
    for page in range(pdf.getNumPages()):
        wr = PdfFileWriter()
        wr.addPage(pdf.getPage(page))

        output = f'data/tmp{page}.pdf'
        with open(output, 'wb') as f:
            wr.write(f)
##pdf_split()

def pdf_merge():
    wr = PdfFileWriter()
    files = ['data/hello.pdf', 'data/sample.pdf']
    for file in files:
        pdf = PdfFileReader(file)
        for page in range(pdf.getNumPages()):
            wr.addPage(pdf.getPage(page))

    with open('tmp/tmp.pdf', 'wb') as f:
        wr.write(f)
##pdf_merge()

def pdf_crop():
    pdf = PdfFileReader('data/sample.pdf')
    p0 = pdf.getPage(0)
    print(p0.mediaBox)              # RectangleObject([0, 0, 612, 792])
    print(p0.mediaBox.lowerLeft)    # (0, 0)
    print(p0.mediaBox.lowerRight)   # (612, 0)
    print(p0.mediaBox.upperLeft)    # (0, 792)
    print(p0.mediaBox.upperRight)   # (612, 792)

    p0.mediaBox.lowerLeft = (0, 500)
    p0.mediaBox.lowerRight = (500, 500)
    
    wr = PdfFileWriter()
    wr.addPage(p0)
    with open('data/tmp.pdf', 'wb') as f:
        wr.write(f)    
##pdf_crop()

def pdf_extract():
    pdf = PdfFileReader('data/students.pdf')
    p0 = pdf.getPage(0)
    with open('data/tmp.txt', 'wb') as f:
        f.write(p0.extractText().encode())
##pdf_extract()

def pdf_watermark():
    wm = PdfFileReader('data/john.pdf').getPage(0)
    pdf = PdfFileReader('data/sample.pdf')
    p0 = pdf.getPage(0)
    p0.mergePage(wm)
    wr = PdfFileWriter()
    wr.addPage(p0)
    with open('tmp/tmp.pdf', 'wb') as f:
        wr.write(f)
##pdf_watermark()

def pdf_encrypt():
    wr = PdfFileWriter()
    pdf = PdfFileReader('data/sample.pdf')
    for page in range(pdf.getNumPages()):
        wr.addPage(pdf.getPage(page))

    # Encrypt:
    wr.encrypt(user_pwd='hello123')
    with open('tmp/tmp1.pdf', 'wb') as f:
        wr.write(f)

    # Decrypt:
    pdf = PdfFileReader('data/tmp1.pdf')
    pdf.decrypt(password='hello123')
    wr = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        wr.addPage(pdf.getPage(page))
    with open('tmp/tmp2.pdf', 'wb') as f:
        wr.write(f)    
##pdf_encrypt()

#---------------------------------------------------------

# pip install reportlab

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4, LETTER, LEGAL, TABLOID
from reportlab.lib.colors import red, green, blue
def pdf_create():
    # Create Canvas:
##    c = Canvas('tmp/hello.pdf')
##    c = Canvas('tmp/hello.pdf', pagesize=A4)
    c = Canvas('tmp/hello.pdf', pagesize=(200, 150))

    # Courier, Courier-Bold, Courier-BoldOblique, Courier-Oblique
    # Helvetica, Helvetica-Bold, Helvetica-BoldOblique, Helvetica-Oblique
    # Times-Roman, Times-Bold, Times-BoldItalic, Times-Italic
    c.setFont('Courier', 18)
    c.setFillColor(red)
    c.drawString(50, 50, 'Hello!')
    c.save()
##pdf_create()
