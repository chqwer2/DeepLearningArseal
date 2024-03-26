from PyPDF2 import PdfFileMerger
import os

files = os.listdir()  # 列出目录中的所有文件
merger = PdfFileMerger()

a = r'C:\Users\calvchen\Desktop\CSC\RP\1.pdf'
b = r'C:\Users\calvchen\Desktop\CSC\RP\2.pdf'
c = r'C:\Users\calvchen\Desktop\CSC\RP\3.pdf'

merger.append(open(a, 'rb'))
merger.append(open(b, 'rb'))
merger.append(open(c, 'rb'))

with open(r'C:\Users\calvchen\Desktop\CSC\RP\ResearchProposal.pdf', 'wb') as fout:
    merger.write(fout)
