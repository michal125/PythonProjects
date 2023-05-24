from pdf2docx import Converter
print("Give name document name in format pdf: ")
pdf_file = input()
print("Give name document name in format docx: ")
docx_file = input()

document = Converter(pdf_file)
document.convert(docx_file)
document.close()

try:
    print("Process Successful")
except NameError:
    print("Error Name")
except ValueError:
    print("Lack value")