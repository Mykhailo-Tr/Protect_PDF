from PyPDF2 import PdfFileWriter, PdfFileReader


def get_data_from_user() -> list:
    infile_path = input("Введіть назву або шлях до файла(my_pdf.pdf): ")
    password = input("Введіть пароль: ")
    outfile_name = input("Введіть назву вихідного файла(protected.pdf): ")

    return [infile_path, outfile_name, password]


def protect_pdf(infile, outfile, password) -> None:
    pdfwriter = PdfFileWriter()
    pdf = PdfFileReader(infile)

    for page in range(pdf.numPages):
        pdfwriter.add_page(pdf.pages[page])

    pdfwriter.encrypt(password)

    with open(outfile, 'wb') as file:
        pdfwriter.write(file)


def main():
    data = get_data_from_user()
    protect_pdf(data[0], data[1], data[2])


if __name__ == '__main__':
    main()
