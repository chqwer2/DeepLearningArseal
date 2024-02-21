from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os



a = r'C:\Users\calvchen\Documents\fr_pdf\FR_combined_drop2.pdf'
pdf_input = PdfFileReader(open(a, 'rb'))

pdf_output = PdfFileWriter()  # 实例一个 PDF文件编写器



for i in range(19):
    if i not in [0, 1, 2, 10, 11, 12, 9, 13, 14, 15]:
        pdf_output.addPage(pdf_input.getPage(i))



with open(r'C:\Users\calvchen\Documents\fr_pdf\FR_combined_drop3.pdf', 'wb') as sub_fp:
    pdf_output.write(sub_fp)