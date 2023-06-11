# -*- coding: utf-8 -*-
"""
@author: Alexander Cheprasov
"""

import sys
sys.path.append('./venv/lib/python3.7/site-packages')
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf

ODD_EVEN_PAGE_FIXER = 1

if __name__ == '__main__':
    print('GO')

if len(sys.argv) != 3:
    print('Please provide path to PDF and name of output file')
    exit(0)

def run(src, dst):
    sourceFile = open(src, 'r+b')
    outputFile = open(dst, 'w+b')

    input = PdfFileReader(sourceFile)
    output = PdfFileWriter()

    for i in range(input.getNumPages()):
        print('Page ', i)
        if (i % 4 == 0):
            pass
        elif (i % 4 == 3):
            output.addPage(input.getPage(i));
            output.addPage(input.getPage(i - 3));
        else:
            output.addPage(input.getPage(i));

    output.write(outputFile)
    sourceFile.close()
    outputFile.close()

run(sys.argv[1], sys.argv[2])