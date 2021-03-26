#ceasor cipher method encryption 
#this is trial module to easy encrypyt the message 
#c=(x-n)%26 we are ging to follow this equation for encrytion
#c is encryted text x is the char n is the shifting key that should be in numbers % is modulus 26 is total alphabets

#function for encrytion
 
def encryption(string,shift):

    cipher=''
    for char in string:
        if char=='':
            cipher=cipher+char
        elif char.isupper():
            cipher=cipher+chr((ord(char)+shift-65)%26+65)
        else:
            cipher=cipher+chr((ord(char)+shift-97)%26+97)
    return cipher

def decryption(string,shift):

    cipher1=''
    for char in string:
        if char=='':
            cipher1=cipher1+char
        elif char.isupper():
            cipher1=cipher1+chr((ord(char)-shift-65)%26+65)
        else:
            cipher1=cipher1+chr((ord(char)-shift-97)%26+97)
    return cipher1
ascii_text=''
text=input("Enter your text here ")
for i in text:
    ascii_text=ascii_text+int(i)
print(ascii_text)
s=int(input("enter the desired shifting key "))
print("the original text was ",text)
print("the encrypted message is ",encryption(text,s))
en=encryption(text,s)
print("The encrypted message is ",en)
print("decrypted message is ",decryption(en,s))