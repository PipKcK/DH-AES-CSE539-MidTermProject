# Author                : Ujjwal Baranwal
# Date                  : November 3, 2023
# Class                 : CSE 539 Applied Cryptography Fall (2023)
# Professor             : Ni Trieu
# Description           : 

# Usage                 : Copy Paste 'Example Usage's Input' on terminal to get the 'Example Usage's Output'
# General Usage's Input : python dhce_main.py initialization vector, g_e, g_c, N_e, N_c, x, g^y mod N, encrypted message C, plaintext P
# Example Usage's Input : python dhce_main.py "A2 2D 93 61 7F DC 0D 8E C6 3E A7 74 51 1B 24 B2" 251 465 255 1311 2101864342 8995936589171851885163650660432521853327227178155593274584417851704581358902 "F2 2C 95 FC 6B 98 BE 40 AE AD 9C 07 20 3B B3 9F F8 2F 6D 2D 69 D6 5D 40 0A 75 45 80 45 F2 DE C8 6E C0 FF 33 A4 97 8A AF 4A CD 6E 50 86 AA 3E DF" AfYw7Z6RzU9ZaGUloPhH3QpfA1AXWxnCGAXAwk3f6MoTx
# General Usage's Output: decrypted text, encrypted cipher
# Example Usage's Output: uUNX8P03U3J91XsjCqOJ0LVqt4I4B2ZqEBfX1gCGBH4hH, 3D E9 B7 31 42 D7 54 D8 96 12 C9 97 01 12 78 F7 A2 4F 69 1A FF F4 42 99 13 A1 BD 73 52 E5 48 63 33 7A 39 BF C5 25 AD 53 26 53 0D E4 81 51 D1 3E

import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# source function sources the values of IV, g, N, x, gy, C and P from the command line
def source():
    # actual function calculates the bigger value using (2^e)-c formula.
    def actual(e,c):
        return 2**e-c
    
    # converting hexadecimal string to a bytes object
    IV = bytes.fromhex(sys.argv[1])
    # calculating the actual g and N values as integers
    g = actual(int(sys.argv[2]),int(sys.argv[3]))
    N = actual(int(sys.argv[4]),int(sys.argv[5]))
    # sourcing x and gy as integers
    x = int(sys.argv[6])
    gy = int(sys.argv[7])
    # converting hexadecimal string to a bytes object
    C = bytes.fromhex(sys.argv[8])
    # sourcing P as a string and converting it to a byte object
    P = sys.argv[9].encode()

    return IV,g,N,x,gy,C,P

def calculateSharedKey(gy, x, N):
    # X = gx = g^x mod N
    # Y = gy = g^y mod N
    # shared key = gy^x mod N = gx^y mod N
    sharedKey = pow(gy, x, N)
    return sharedKey

# encrypt function encrypts the plain text using AES-CBC mode and returns the cipher text
def encrypt(plainText, sharedKey, IV):
    # creates a new AES object with the given key, mode and IV
    cipher = AES.new(sharedKey, AES.MODE_CBC, IV)
    cipheredText = cipher.encrypt(pad(plainText, AES.block_size)).hex()
    return cipheredText

# decrypt function decrypts the cipher text using AES-CBC mode and returns the plain text
def decrypt(cipherText, sharedKey, IV):
    # creates a new AES object with the given key, mode and IV
    decipher = AES.new(sharedKey, AES.MODE_CBC, IV)
    decipheredText = unpad(decipher.decrypt(cipherText), AES.block_size).decode()
    return decipheredText

# main
if __name__ == "__main__":
    # source the values of IV, g, N, x, gy_modN, given_cipherText, given_plainText
    IV, g, N, x, gy_modN, given_cipherText, given_plainText = source()

    # calculated shared key, specified key length and set byteorder to little 
    key = calculateSharedKey(gy_modN, x, N).to_bytes(32, byteorder='little')

    # encrypted and decrypted the given plain text and cipher text
    cipheredText, decipheredText = encrypt(given_plainText, key, IV), decrypt(given_cipherText, key, IV)

    # formatted and printed the output (decipheredText, cipheredText)
    print('{}, {}'.format(decipheredText, " ".join([cipheredText.upper()[i:i+2] for i in range(0, len(cipheredText), 2)])))


