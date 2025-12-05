import hashlib
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcdExtended(a, b):
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
    print(gcd(24,36))
    print(gcdExtended(24,36))
    print(math.gcd(24,36))

if __name__ == "__main__":
    main()