from PyPDF2 import PdfMerger
import os
from PyPDF2 import PdfWriter, PdfReader

files = os.listdir()  # 列出目录中的所有文件
merger = PdfMerger()

a = '/Users/haochen/Desktop/CSC_Guangdong/CSC_File.pdf'
b = '/Users/haochen/Desktop/CSC_Guangdong/CSC_14_15_13.pdf'
c = "pdf"
out = '/Users/haochen/Desktop/CSC_Guangdong/CSC_File_combine.pdf'

merger.append(open(a, 'rb'))
merger.append(open(b, 'rb'))
merger.append(open(c, 'rb'))

# with open(r'C:\Users\calvchen\Downloads\UoB.pdf', 'wb') as fout:
#     merger.write(fout)


# combine
inputpdf_a = PdfReader(open(a, "rb"))
inputpdf_b = PdfReader(open(b, "rb"))
output = PdfWriter()

for i in range(len(inputpdf_a.pages)):
    if i >= 11:
        break
    output.add_page(inputpdf_a.pages[i])
    
output.add_page(inputpdf_b.pages[-1])
output.add_page(inputpdf_b.pages[0])
output.add_page(inputpdf_b.pages[1])
output.add_page(inputpdf_a.pages[-1])
    
with open(out, "wb") as outputStream:
    output.write(outputStream)




print("Done...")
