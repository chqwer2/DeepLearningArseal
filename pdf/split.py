



pdf = r"C:\Users\calvchen\Downloads/MICCAI_2024_Domain_Generalization (2).pdf"



from PyPDF2 import PdfWriter, PdfReader

inputpdf = PdfReader(open(pdf, "rb"))



first = 10

main = PdfWriter()
supp = PdfWriter()





for i in range(len(inputpdf.pages)):
    if i < first:
        main.add_page(inputpdf.pages[i])
    else:
        supp.add_page(inputpdf.pages[i])



#
# with open("plot_%s.pdf" % (i+1), "wb") as outputStream:
#     output.write(outputStream)


with open("MICCAI_2024_Domain_Generalisation_main.pdf", "wb") as outputStream:
    main.write(outputStream)



with open("MICCAI_2024_Domain_Generalisation_supp.pdf", "wb") as outputStream:
    supp.write(outputStream)

