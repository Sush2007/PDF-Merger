from pypdf import PdfWriter
import os

merger = PdfWriter()
pdfs = []
n = int(input("Enter number of PDFs to merge: "))
for i in range(n):
    name = input(f"Enter the path of PDF {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    try:
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"Error: The file '{pdf}' was not found. Skipping.")
    except Exception as e:
        print(f"An error occurred with file '{pdf}': {e}")


merger.write("merged-pdf.pdf")
merger.close()
print("PDFs merged successfully into merged-pdf.pdf")