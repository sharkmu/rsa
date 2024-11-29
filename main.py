from sympy import nextprime
from random import getrandbits
import random
import os

def text_to_numbers(text): # ASCII
    return [ord(char) for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num) for num in numbers])

def break_fn():
    input()
    os.system("cls")

bits = random.randint(100, 200) # generate_prime()
def generate_prime(bits): # titkos
    random_number = getrandbits(bits)
    prime = nextprime(random_number)
    return prime

def n_func(p, q): # nyilvános
    return p * q


p = generate_prime(bits)
q = generate_prime(bits)

while q is p:
    q = generate_prime(bits)

n = n_func(p, q)

m = (p - 1) * (q - 1) # Euler


def euklideszi_gcd(a, b): # Euklideszi algoritmus (nagyobb közös osztó)
    while b:
        a, b = b, a % b
    return a


def generate_random_e(m): # relatív prím az m-el
    while True:
        e = random.randint(2, m - 1)
        if euklideszi_gcd(e, m) == 1:
            return e

e = generate_random_e(m)




def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

def mod_inverse(e, m):
    g, x, y = extended_gcd(e, m)
    return x % m


d = mod_inverse(e, m)

def mod_encrypt(x, e, n):
    return pow(x, e, n)

def mod_decrypt(y, d, n):
    return pow(y, d, n)



text = str(input("Add meg a titkosítani kívánt szöveget! "))
txt_ascii = text_to_numbers(text)


# encrypt
encrypted_numbers = [mod_encrypt(num, e, n) for num in txt_ascii]
print(f"Titkosított szöveg: {encrypted_numbers}")
break_fn()

# decrypt
decrypted_numbers = [mod_decrypt(num, d, n) for num in encrypted_numbers]
decrypted_text = numbers_to_text(decrypted_numbers)
print(f"Visszafejtett szöveg: {decrypted_text}")