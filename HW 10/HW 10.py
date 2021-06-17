import pyAesCrypt
def enc(filename,password):
    pyAesCrypt.encryptFile(filename, (filename + ".enc"), password)

def dec(filename,password):
    f = filename[:-4]
    pyAesCrypt.decryptFile(filename, f, password)

a=int(input("Press 1 to enc and 0 for dec: "))
filename=input("Enter file name: ")
password=input("Enter password: ")

if(a==1):
    enc(filename,password)
elif(a==0):
    dec(filename,password)
else:
    print("Incorrect choice")