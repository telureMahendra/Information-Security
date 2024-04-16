import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from PyPDF2 import PdfReader, PdfWriter

def generate_signature(data):
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    # Sign the data
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature, public_key

def verify_signature(signature, data, public_key):
    # Verify the signature
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print("Signature verification failed:", e)
        return False

def add_signature_to_pdf(input_pdf, output_pdf, signature, public_key):
    # Read the input PDF
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    # Add signature data to metadata
    pdf_writer.add_metadata({
        '/Signature': signature,
        '/PublicKey': public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    })

    # Add pages from input PDF to output PDF
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write output PDF with signature
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    # Data to sign
    data = b"Example data to sign"

    # Generate signature and public key
    signature, public_key = generate_signature(data)

    # Verify the signature
    if verify_signature(signature, data, public_key):
        print("Signature verified successfully!")
    else:
        print("Signature verification failed!")

    # Add signature to a PDF
    input_pdf = "input.pdf"
    output_pdf = "output_signed.pdf"
    add_signature_to_pdf(input_pdf, output_pdf, signature, public_key)
