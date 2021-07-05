import hashlib

def Md5_convert(text):
   Hash = hashlib.md5()
   Hash.update(text.encode('utf-8'))
   print(Hash.hexdigest())

text = input("Enter Your text: ")

Md5_convert(text)
