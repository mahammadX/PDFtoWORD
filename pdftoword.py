#Programmer : Eng. Mahammad Qassem
from pdf2docx import Converter

pdf_file = input("Name file pdf : ")

docx_file = input("Name file docx : ")

conv = Converter(pdf_file)
conv.convert(docx_file)

conv.close()