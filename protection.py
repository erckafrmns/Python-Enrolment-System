import os
import random

# Get the parent folder of the root folder
parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_key():
    bin_fp = os.path.join(parent_folder, "[PY] UNI_ENROLL_SYS", "DATABASE", "3", "3.bin")

    with open(bin_fp, 'rb') as file:
        encoded_data = file.read()
        data = encoded_data.decode()
        return int(data)
    
nsm = random.randint(1, 5)
osm = load_key()

def encrypt(txt):
    new_txt = ""

    for char in txt:
        new_char = new_char = chr(ord(char) + nsm)
        new_txt += new_char

    return new_txt

def encrypt_w_ok(txt):
    new_txt = ""

    for char in txt:
        new_char = new_char = chr(ord(char) + osm)
        new_txt += new_char

    return new_txt

def decrypt(txt):
    new_txt = ""

    for char in txt:
        new_char = new_char = chr(ord(char) - osm)
        new_txt += new_char

    return new_txt