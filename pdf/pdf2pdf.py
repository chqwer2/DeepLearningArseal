from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os



a = r'C:\Users\calvchen\Downloads\sainsburys-ar2021.pdf'
pdf_input = PdfFileReader(open(a, 'rb'))

pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器

for i in range(101, 106):
    pdf_output.addPage(pdf_input.getPage(i))

with open(r'C:\Users\calvchen\Downloads\sainsburys-102page.pdf', 'wb') as sub_fp:
    pdf_output.write(sub_fp)