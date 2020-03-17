"""Encrypt and decrypt message."""

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
    if open_file_read("mynewprimes.txt"):
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
        if r != chosen_funn and str(r) in list_primes:
            if 2 < r < chosen_funn:
                break
    return r


# egcd and mod_mul_inv borrowed from SO.


def egcd(a, b):
    """Get GCD."""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b//a) * y, y)


def mod_mul_inv(a, m):
    """Get modInv."""
    g, x, _ = egcd(a, m)
    return x % m


def encrypt_pub(m, n, e):
    """Encrypt message m."""
    enc_m = pow(m, e, n)
    return enc_m


def decrypt(c, n, d):
    """Decrypt message c."""
    dec_c = pow(c, d, n)
    return dec_c


def assign_primes(primes):
    """Assign random large primes."""
    p = int(primes[randint(0, len(primes) - 1)])
    while True:
        q = int(primes[randint(0, len(primes) - 1)])
        if p != q:
            break
    return p, q


def encrypt(num_message):
    """Encrypt message, return cipher."""
    list_primes = prime()
    p, q = assign_primes(list_primes)
    n = p * q
    phi = totient(p, q)
    e = coprime(list_primes, phi)
    d = mod_mul_inv(e, phi)
    enc = encrypt_pub(num_message, n, e)
    priv_key = f"{n},{d},"
    return enc, priv_key
