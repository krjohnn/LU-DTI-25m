import hashlib
import math
import random
import base64


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcdExtended(a, b) -> list:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_keys(p, q):
    return

def main():
    print("Start")

    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 5
    print(f"n is {n}, phi is: {phi}, e is: {e}")

    g, d, y = gcdExtended(e,phi)
    print(g, d, y)
    d = d % phi

    print(f"Public key: {e, n}, Private key: {d, n}")

    msg=23
    print(msg)
    C=pow(msg,e)%n
    print(f"msg is {msg}, C is {C}")

    M=pow(C,d)%n
    print(f"msg is {msg}, M is {M}")

if __name__ == "__main__":
    main()