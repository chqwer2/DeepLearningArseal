from PyPDF2 import PdfFileMerger
import os

files = os.listdir()  # 列出目录中的所有文件
merger = PdfFileMerger()

a = r'C:\Users\calvchen\Downloads\UoB_Cover.pdf'
b = r'C:\Users\calvchen\Downloads\NoisyRepresentation.pdf'

merger.append(open(a, 'rb'))
merger.append(open(b, 'rb'))

with open(r'C:\Users\calvchen\Downloads\UoB.pdf', 'wb') as fout:
    merger.write(fout)
