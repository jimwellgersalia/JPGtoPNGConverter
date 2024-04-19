import PyPDF2
from sys import argv

inputs = argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
    

pdf_combiner(inputs)


# # rb stands for read binary as pdf is a binary
# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     # page = reader.pages[0]
#     # page.rotate(90)
# with open('new.pdf', 'wb') as new_file:
#     writer = PyPDF2.PdfWriter()
#     writer.write(new_file)
