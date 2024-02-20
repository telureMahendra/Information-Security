# Program 4
# Aim :  Implement HASHING algorithm 

import hashlib 
# initializing string 
str = "Government college of engineering"
  
# encoding "Government college of engineering" using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode())

print("Printing hash value of: ", str ) 
print(result)
print ("\n") 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  
# initializing string 
str = "Government college of engineering"
  
# encoding Government college of engineering using encode() 
# then sending to SHA384() 
result = hashlib.sha384(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA384 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  
# initializing string 
str = "Government college of engineering"
  
# encoding Government college of engineering using encode() 
# then sending to SHA224() 
result = hashlib.sha224(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA224 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  
# initializing string 
str = "Government college of engineering"
  
# encoding Government college of engineering using encode() 
# then sending to SHA512() 
result = hashlib.sha512(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA512 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  
# initializing string 
str = "Government college of engineering"
  
# encoding Government college of engineering using encode() 
# then sending to SHA1() 
result = hashlib.sha1(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 is : ") 
print(result.hexdigest())
