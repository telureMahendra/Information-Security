
 #Program 5
#To make digital signiture

from ecdsa import SigningKey
private_key = SigningKey.generate()
signature = private_key.sign(b"creating a digital signature")
print(signature)
