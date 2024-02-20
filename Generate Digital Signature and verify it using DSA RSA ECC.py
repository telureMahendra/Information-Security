# Practical 6:
# Aim: Generate Digital Signature and verify it using DSA/RSA/ECC

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(2048)
f = open("public_key.pem","wb")
f.write(key.public_key().export_key())
f.close()

messege = b"Hemant"
hash_obj = SHA256.new(messege)
signer = DSS.new(key,'fips-186-3')
signature = signer.sign(hash_obj)

f = open("public_key.pem","r")
hash_obj = SHA256.new(messege)
pub_key = DSA.import_key(f.read())
verifire = DSS.new(pub_key,'fips-186-3')

try :
    verifire.verify(hash_obj,signature)
    print("The Message Is Authenticate")
except ValueError:
    print("The Message is not authenticate")
