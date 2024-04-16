from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

def generate_rsa_keypair():
    # Generate RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def generate_rsa_signature(data, private_key):
    # Generate RSA signature
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_rsa_signature(signature, data, public_key):
    # Verify RSA signature
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

# Example usage
data = b"Hello, this is some data to sign and verify!"
private_key, public_key = generate_rsa_keypair()
signature = generate_rsa_signature(data, private_key)
print("Generated Signature:", signature.hex())

# Verify the signature
if verify_rsa_signature(signature, data, public_key):
    print("Signature verification successful!")
else:
    print("Signature verification failed!")
