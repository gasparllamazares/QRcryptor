from cryptography.fernet import Fernet
from time import sleep
from random import uniform
from tqdm import tqdm
import pyfiglet
import keyboard
import os
from termcolor import colored, cprint
from pynput.keyboard import Key, Controller

# long process here

while True:

    print(" \n")

    ascii_banner = pyfiglet.figlet_format("Uniovi  Decoder")
    print(ascii_banner)
    encrypted = input('Introducir QR cifrado: ')
    print("")
    f2 = Fernet(b'gwi9ACyzHI87zhl5wYM1GOJlZhOePAZl4K3obyHWB4w=')
    try:
        f2.decrypt(encrypted.encode())
    except:
        for _ in tqdm(range(1000), unit=' Verifications'):
            sleep(uniform(0.0000001, 0.0000001))

        cprint('\nCódigo QR no válido', 'red', attrs=['blink', 'bold'])
    else:
        decrypted = f2.decrypt(encrypted.encode())
        for _ in tqdm(range(1000), unit=' Verifications'):
            sleep(uniform(0.005, 0.01))
        cprint(f'\nNúmero del QR: {decrypted.decode()}', 'green')
    print("")
    print("Press Y to continue, press esc to exit")
    if keyboard.read_key() == "y":
        os.system('cls')
        keyboard.press('del')
        keyboard.release('del')
    if keyboard.read_key() == "esc":
        break
