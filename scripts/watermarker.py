import PyPDF2


template = PyPDF2.PdfFileReader(open('filename.pdf', 'rb')) # pdf to be edited goes here
watermark = PyPDF2.PdfFileReader(open('filename.pdf', 'rb')) # pdf with watermark goes here
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('output_filename.pdf', 'wb') as file_output:
    output.write(file_output)
