# -*- coding: utf-8 -*-
"""
@author: Alexander Cheprasov
PDF-splitter for my e-reader Sony PRS-T2
"""

import sys
import copy
import math
sys.path.append('./venv/lib/python3.7/site-packages')
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf


if __name__ == '__main__':
    print('GO')

def join_pdf(output, filename):
    sourceFile = open(filename, 'r+b')
    input = PdfFileReader(sourceFile, strict=False)

    for i in range(input.getNumPages()):
        page = input.getPage(i)
        pageCopy = copy.copy(page)
        pageCopy.mediaBox = copy.copy(page.cropBox)
        pageCopy.artBox = pageCopy.mediaBox
        pageCopy.bleedBox = pageCopy.mediaBox
        pageCopy.cropBox = pageCopy.mediaBox
        output.addPage(pageCopy)

    sourceFile.close()

def split_pages2():
    outputFile = open('./deti.pdf', 'w+b')
    output = PdfFileWriter()

    join_pdf(output, './deti/A4_Pages_1.pdf')
    join_pdf(output, './deti/A4_Pages_2.pdf')
    join_pdf(output, './deti/A4_Pages_3.pdf')
    join_pdf(output, './deti/A4_Pages_4.pdf')
    join_pdf(output, './deti/A4_Pages_5.pdf')
    join_pdf(output, './deti/A4_Pages_6.pdf')
    join_pdf(output, './deti/A4_Pages_7.pdf')
    join_pdf(output, './deti/A4_Pages_8.pdf')

    output.write(outputFile)
    outputFile.close()

split_pages2()