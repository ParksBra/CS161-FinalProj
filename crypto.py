"""Encrypt and decrypt message."""

import binascii
import hashlib
from random import randint
import sys


def open_file_read(filename):
    """Read file."""
    try:
        with open(str(filename), "r") as open_file:
            return open_file.read()
        open_file.close()
    except FileNotFoundError:
        return False


def prime():
    """Get list of primes from file made using sage."""
    if not open_file_read("mynewprimes.txt") == False:
        raw_file = str(open_file_read("mynewprimes.txt"))
        primes = [i.strip() for i in raw_file.split(",")]
        return primes
    else:
        print("Error: mynewprimes.txt not found.")
        sys.exit()
    

def totient(p, q):
    """Compute totient of p and q."""
    return ((p - 1) * (q - 1))


def coprime(list_primes, chosen_funn):
    """Find random coprime."""
    while True:
        r = int(list_primes[randint(0, len(list_primes) - 1)])
        # print(r) Testing
        if r != chosen_funn and str(r) in list_primes:
            if 2 < r < chosen_funn:
                break
    return r


#egcd and mod_mul_inv borrowed from SO
def egcd(a, b):
    """Get GCD."""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)
    

def mod_mul_inv(m, a):
    """Get modInv."""
    g, x, y = egcd(a, m)
    return x%m


def encrypt_pub(m, n, e):
    """Encrypt message m."""
    enc_m = pow(m, e, n)
    return enc_m


def decrypt(c, n, d):
    """Decrypt message c."""
    dec_c = pow(c, d, n)
    return dec_c


def main():
    """Initialize program, m is message to encrypt."""
    # print(f"{hashlib.sha1(b'Hello World').hexdigest()}is the message hash to hex")
    # m = (int(hashlib.sha1(b'Hello World').hexdigest(), 16))
    m = 12345  # Testing
    # print(f"{m} is the message after hash to decimal")
    # m = int(binascii.hexlify(binascii.a2b_uu("Hello")), 16)
    list_primes = prime()
    p = int(list_primes[randint(0, len(list_primes) - 1)])
    while True:
        q = int(list_primes[randint(0, len(list_primes) - 1)])
        if p != q:
            break
    n = p * q
    nt = totient(p, q)
    e = coprime(list_primes, nt)
    d = mod_mul_inv(nt, e)
    enc = encrypt_pub(m, n, e)
    dec = decrypt(enc, n, d)
    # print(p, q, n, nt, e, d)
    # print(f"{dec} is the decrypted message in decimal")
    # print(f"{enc} is the encrypted message in decimal")
    dec_hex = hex(dec)
    print(f"{dec_hex} is the decrypted message in hex")
    # print(mod_mul_inv(72, 23))


if __name__ == "__main__":
    main()
