# Practical 1
# Aim: Build the program where user-entered text is encrypted using caeser cipher algorithm.

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
playing = ''
final = ''
org = ''
def encrypt(str,n): 
    result = [] 
    for x in str: 
        if x == " ": 
            converted = ''
            result.append(converted) 
        else: 
            converted = (letters.index(x) +n) %26 
            result.append(letters[converted]) 
            final = ''.join(result) 
    print(final) 
    return final 
def decrypt(str,n): 
    back = [] 
    for x in str: 
        if x == " ": 
            original = '' 
            back.append(original) 
        else: 
            original = (letters.index(x) -n) %26 
            back.append(letters[original]) 
            org = ''.join(result) 
    print(org)
    
str=input("enter the string to be encrypted") 
n=int(input("enter the key")) 
final=encrypt(str,n) 
print("let’s decrypt the text") 
decrypt(final,n)

