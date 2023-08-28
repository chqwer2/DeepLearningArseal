from PyPDF2 import PdfFileMerger
import os

files = os.listdir()  # 列出目录中的所有文件
merger = PdfFileMerger()

a = r'C:\Users\calvchen\Desktop\HaoChen-CV\春招实习_陈皓.pdf'
b = r'C:\Users\calvchen\Desktop\HaoChen-CV\CV_3.4_eng.pdf'

merger.append(open(a, 'rb'))
merger.append(open(b, 'rb'))

with open(r'C:\Users\calvchen\Desktop\HaoChen-CV\2022春招\ChenHao-CV.pdf', 'wb') as fout:
    merger.write(fout)
