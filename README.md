# QRcryptor
QR encrypted data generator


Files:
  QRnumberGEN: generates and encrypts numbers in a range from 0 to 1000 (usually for lottery tickets to prevent forgery) and then
    generates QR codes with each crypted number and saves them
        Modules used: qrcode, cryptography, PIL
    
  QRdecryptor: decrypts QR crypted texts with given key, .exe file created with auto-py-to-exe, it also contains some garnish
     in order for the .exe file look better
        Modules used: Cryptography, time, random, tqdm, pyfiglet, keyboard, os, termcolor, pynput
      
  
