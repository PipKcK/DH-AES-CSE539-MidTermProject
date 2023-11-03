# CSE 539 Applied Cryptography Fall (2023)

*Mid-term Exam*

---

## Diffie-Hellman and Encryption Project

This repository contains the implementation of a Diffie-Hellman Cryptosystem Encryption (DHCE) program in Python. The program was developed by Ujjwal Baranwal for the CSE 539 Applied Cryptography course in Fall 2023, under the guidance of Professor Ni Trieu.

## Description

The program implements a Diffie-Hellman key exchange protocol to generate a shared secret key between two parties. It then uses this key to encrypt and decrypt messages using the AES-CBC mode.

## Requirements

This project requires `Python 3.11` version or higher.
This project requires `pycryptodome` version `3.19.0`.

#### Installation

1. [Download Python](https://www.python.org/downloads/) for your specific usage.
2. To install the latest version of pycryptodome use 
    + `pip install pycryptodome` or `pip3 install pycryptodome`
> Note: In some uncommon scenarios, even with `pycryptodome` installed, the execution of the project might result in an error stating `ModuleNotFoundError: No module named 'Crypto'`.
To resolve this use the following commands.
`pip uninstall crypto`
`pip uninstall pycryptodome`
`pip install pycryptodome`

## Usage

To use this script, you need to provide several parameters as command line arguments.

#### General Input

```bash
python dhce_main.py initialization vector, g_e, g_c, N_e, N_c, x, g^y mod N, encrypted message C, plaintext P
```

#### General Output

```
decrypted text, encrypted text
```

#### Example Input:

```bash
python dhce_main.py "A2 2D 93 61 7F DC 0D 8E C6 3E A7 74 51 1B 24 B2" 251 465 255 1311 2101864342 8995936589171851885163650660432521853327227178155593274584417851704581358902 "F2 2C 95 FC 6B 98 BE 40 AE AD 9C 07 20 3B B3 9F F8 2F 6D 2D 69 D6 5D 40 0A 75 45 80 45 F2 DE C8 6E C0 FF 33 A4 97 8A AF 4A CD 6E 50 86 AA 3E DF" AfYw7Z6RzU9ZaGUloPhH3QpfA1AXWxnCGAXAwk3f6MoTx
```

#### Example Output

```bash
uUNX8P03U3J91XsjCqOJ0LVqt4I4B2ZqEBfX1gCGBH4hH, 3D E9 B7 31 42 D7 54 D8 96 12 C9 97 01 12 78 F7 A2 4F 69 1A FF F4 42 99 13 A1 BD 73 52 E5 48 63 33 7A 39 BF C5 25 AD 53 26 53 0D E4 81 51 D1 3E
```

## Screenshots
1. Screenshot 1
![image info](./Screenshots/Screenshot%202023-11-03%20013515.png)
2. Screenshot 2
![image info](./Screenshots/Screenshot%202023-11-03%20124437.png)

## Credits

| Author | Professor | Class | Date |
|--------|-----------|-------|------|
| **Ujjwal Baranwal** | Ni Trieu | CSE 539-Applied Cryptography (Fall 2023)|November 3rd, 2023

