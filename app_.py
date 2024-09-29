from PyPDF2 import PdfReader, PdfWriter

# Replace '' with the path to your encrypted PDF file
input_pdf_path = r''
# Replace '' with the path where you want to save the decrypted PDF
output_pdf_path = r''
# Replace '' with the known password of the PDF
password = ''

# Open the encrypted PDF
reader = PdfReader(input_pdf_path)
reader.decrypt(password)

# Create a PdfWriter object and add the decrypted pages
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

# Save the decrypted PDF to a new file
with open(output_pdf_path, 'wb') as output_pdf:
    writer.write(output_pdf)

print("Password removed successfully. Decrypted file saved as:", output_pdf_path)
