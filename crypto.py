"""Encrypt and decrypt message."""

import hashlib
from random import randint


def prime(minnum, maxnum):
    """Return list of primes."""
    primes = []
    for o in range(minnum, maxnum + 1):
        if o > 1:
            for i in range(2, o):
                if o % i == 0:
                    break
            else:
                primes.append(o)
    return primes


def totient(p, q):
    """Compute totient of p and q."""
    return ((p - 1) * (q - 1))


def coprime(list_primes, chosen_funn):
    """Find random coprime."""
    while True:
        r = randint(2, chosen_funn - 1)
        # print(r) Testing
        if r != chosen_funn and r in list_primes:
            break
    return r


def mod_mul_inv(n, e):
    """Create dumb number."""
    x = 0
    d = ((1 + (x * n)) / e)
    while not d.is_integer():
        # print("r",d) Testing
        x += 1
        d = ((1 + (x * n)) / e)
        # if d >= 50000000: # Eventually fix forever loop.
    return int(d)


def encrypt_pub(m, n, e):
    """Encrypt message m."""
    enc_m = (pow(m, e) % n)
    return enc_m


def decrypt(c, n, d):
    """Decrypt message c."""
    dec_c = (pow(c, d) % n)
    return dec_c


def main():
    """Initialize program, m is message to encrypt."""
    print(f"{hashlib.sha1(b'Hello World').hexdigest()}is the message hash to hex")
    # m = (int(hashlib.sha1(b'Hello World').hexdigest(), 16))
    m = 12345  # Testing
    print(f"{m} is the message after hash to decimal")
    list_primes = prime(2, 1000)
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
    print(p, q, n, nt, e, d)
    print(f"{dec} is the decrypted message in decimal")
    print(f"{enc} is the encrypted message in decimal")
    dec_hex = hex(dec)
    print(f"{dec_hex} is the decrypted message in hex")
    # print(mod_mul_inv(72, 23))


if __name__ == "__main__":
    main()
