import qrcode
from cryptography.fernet import Fernet
from PIL import ImageShow
file = open('key.key', 'rb') #Here your Fernet key stored in a key.key file
key = file.read()
file.close()
print(key)
for n in range(0,1):
    number = str(n)
    encoded = number.encode()

    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    print(encrypted)
    img = qrcode.make(encrypted)
    img.save(f'No{n}.png')
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted)
