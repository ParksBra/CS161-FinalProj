# CS161-FinalProj
Final project for CS161



Instructions:

Verify you are in project directory

## Encryption:
Run "main.py"

To encrypt, type "e"

Select a .txt file, I made one called "test_file.txt".

Program will let you know if it was successful. 

Check encrypted.txt and key.txt

## Decryption:
Run "main.py"

To decrypt, type "d"

Program will let you know if it was successful.

Check decrypted.txt


-----------------------------------


I did stray away from using hashlib, as my original; proposal said. I instead used codecs. It suited my needs a lot better than hashlib did, since codecs dosen't aid in the actual encryption part of my program.


-----------------------------------


### Credit where credit is due:
I did base a small snippet of code off of something from stack overflow.

To find the modular multipative inverse, I had use my own fabricated code:

```python
def mod_mul_inv(n, e):
    """Create dumb number."""
    x = 0
    d = ((1 + (x * n)) / e)
    while not d.is_integer():
        x += 1
        d = ((1 + (x * n)) / e)
    return int(d)
```

Once I started using much larger prime numbers, this became a very bad bottleneck. I searched and searched for a more efficient solution, and found:

```python
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
```

This was the perfect solution, and after staring at it for a while, I understood it.
