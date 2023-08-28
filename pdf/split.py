



pdf = "C:/Users/calvchen/Downloads/ICCV (1).pdf"



from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open(pdf, "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("plot_%s.pdf" % (i+1), "wb") as outputStream:
        output.write(outputStream)



