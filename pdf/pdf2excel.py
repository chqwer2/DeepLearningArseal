# -*- coding: utf-8 -*-
"""
Created on Fri May 17 2019
@author: YangYang

请确保你在运行这个代码的时候，已经安装了pdfplumber库
如果没有安装，请在[附件-命令提示符]下输入：
pip install pdfplumber
"""

import pdfplumber
import xlwt
import numpy as np
# 定义保存Excel的位置
workbook = xlwt.Workbook()  #定义workbook

# worksheet = workbook.add_sheet("Sheet 1")
i = 0 # Excel起始位置

path = r'C:\Users\calvchen\Downloads\sainsburys-102page.pdf'
#path = "aaaaaa.PDF"  # 导入PDF路径
pdf = pdfplumber.open(path)

print('\n')
print('开始读取数据')
print('\n')
for i, page in enumerate(pdf.pages):
    sheet = workbook.add_sheet('Sheet{}'.format(i), cell_overwrite_ok=True)  # 添加sheet
    # 获取当前页面的全部文本信息，包括表格中的文字
    text = page.extract_text().split('\n')#[6:]

    for i,t in enumerate(text):
        head = ''
        count = -1
        point = 0
        for j,m in enumerate(t.split(' ')):
            if '-' in m:
                sheet.write(i, point, m)
                point += 1

            if m.isalpha() or m.startswith(' '):
                head= head + ' ' + m
                continue
            elif head != '':
                sheet.write(i, point, head)
                head = ''
                point += 1

            if m.strip('(').strip(')').replace(',', '').isalnum():
                sheet.write(i, point, m)
                point += 1
        sheet.write(i, point, head)

    print('---------- 分割线 ----------')

pdf.close()

# 保存Excel表
workbook.save(r'C:\Users\calvchen\Desktop/PDFresult.xls')
print('\n')
print('写入excel成功')
print('保存位置：')
print('C:/Users/Administrator/Desktop/PDFresult.xls')
print('\n')
input('PDF取读完毕，按任意键退出')