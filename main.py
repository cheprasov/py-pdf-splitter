# -*- coding: utf-8 -*-
"""
@author: Alexander Cheprasov
PDF-splitter for my e-reader Sony PRS-T2
"""

import sys
import copy
import math
from PyPDF2 import PdfFileReader, PdfFileWriter, pdf

PAGE_PARTS_COUNT = 3 # todo: calculate by height
PAGE_SIZE_RATE = 0.445 # todo: calculate by width

# todo: move to argv
marginTop = 30
marginBottom = 30
marginLeft = 40
marginRight = 40

# todo: move to arv
marginLeftEven = 10
marginLeftOdd = 0
marginRightEven = 0
marginRightOdd = 10

oddEvenFixer = 1

if __name__ == '__main__':
    print('GO')

if len(sys.argv) != 3:
    print('Please provide path to PDF and name of output file')
    exit(0)

def preparePage(output, page: pdf.PageObject, num: int):
    num += oddEvenFixer
    box = page.mediaBox

    x0, y0 = box.lowerLeft
    x2, y2 = box.upperRight
    x0, y0 = math.floor(x0) + marginLeft, math.floor(y0) + marginTop
    x2, y2 = math.ceil(x2) - marginRight, math.ceil(y2) - marginBottom

    if (num % 2 == 0):
        # Even
        x0 += marginLeftEven
        x2 -= marginRightEven
    else:
        # Odd
        x0 += marginLeftOdd
        x2 -= marginRightOdd

    pageHeight = y2 - y0
    pageWidth = x2 - x0

    # pageHeight = box.up
    for i in reversed(range(PAGE_PARTS_COUNT)):
        pagePart = copy.copy(page)
        pagePart.mediaBox = copy.copy(pagePart.cropBox)

        partHeight = round(PAGE_SIZE_RATE * float(pageHeight))
        y = round(i/(PAGE_PARTS_COUNT - 1) * (pageHeight - partHeight)) + marginBottom

        pagePart.mediaBox.lowerLeft = (x0, y)
        pagePart.mediaBox.upperRight = (x2, y + partHeight)

        pagePart.artBox = pagePart.mediaBox
        pagePart.bleedBox = pagePart.mediaBox
        pagePart.cropBox = pagePart.mediaBox

        output.addPage(pagePart)

def split_pages2(src, dst):
    sourceFile = open(src, 'r+b')
    outputFile = open(dst, 'w+b')

    input = PdfFileReader(sourceFile)
    output = PdfFileWriter()

    for i in range(input.getNumPages()):
        page = input.getPage(i)
        preparePage(output, page, i)

    output.write(outputFile)
    sourceFile.close()
    outputFile.close()

split_pages2(sys.argv[1], sys.argv[2])