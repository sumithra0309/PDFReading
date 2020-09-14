from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path,'rb') as f:
        pdf=PdfFileReader(f)
        number_of_pages=pdf.getNumPages()
        output=""
        for i in range(number_of_pages):
            page=pdf.getPage(i)
            output+=page.extractText()
    return output

def create_file(information):
    with open('myfile.c', 'w') as fp:
        fp.write(information)
    with open('myfile.h', 'w') as fp1:
        fp1.write(information)


if __name__ == '__main__':
    path='report-sample.pdf'
    inform=extract_information(path)
    create_file(inform)

