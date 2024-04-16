from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def encrypt_aes(data, key):
    backend = default_backend()
    
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Pad the data to be encrypted
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    
    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    return iv + encrypted_data

def decrypt_aes(encrypted_data, key):
    backend = default_backend()
    
    # Extract IV from encrypted data
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]
    
    # Create AES cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()
    
    # Decrypt the data
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Unpad the decrypted data
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    
    return unpadded_data

# Example usage
key = os.urandom(32)  # AES-256 key
data = b"Hello, AES encryption and decryption!"

# Encrypt the data
encrypted_data = encrypt_aes(data, key)
print("Encrypted:", encrypted_data)

# Decrypt the data
decrypted_data = decrypt_aes(encrypted_data, key)
print("Decrypted:", decrypted_data.decode())
