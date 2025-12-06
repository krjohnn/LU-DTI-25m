import hashlib
import base64
import math

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def main():
    print("--- ATSLĒGU ĢENERĒŠANA ---")

    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    print(f"n is {n}, phi is: {phi}, e is: {e}")

    g, x, y = gcd_extended(e, phi)
    if g != 1:
        raise ValueError("e and phi are not coprime, choose a different e")
    d = x % phi

    print(f"Publiskā atslēga:  (e={e}, n={n})")
    print(f"Privātā atslēga: (d={d}, n={n})")

    print("--- ALISE PARAKSTĀS ---")

    msg = "KINO"
    print(f"Ziņa: {msg}")

    alise_md5 = hashlib.md5(msg.encode())
    alise_hash_1b = alise_md5.digest()[0]
    print("Alises MD5 1. baits:", alise_hash_1b)

    C = pow(alise_hash_1b, e, n)
    print(f"Encrypted (C) = {C}")

    print("--- EVA UZBRŪK ---")
    new_msg = "KiNO"
    print(f"Jaunā ziņa: {new_msg}")

    print("--- BOBS SAŅEM ---")

    bob_md5 = hashlib.md5(new_msg.encode())
    bob_hash_1b = bob_md5.digest()[0]
    print(f"Boba MD5 1. baits: {bob_hash_1b}")

    M = pow(C, d, n)
    print(f"Decrypted (M) = {M}")

    print("--- REZULTĀTS ---")
    if M == bob_hash_1b:
        print("Ziņojums ir DERĪGS!")
    else:
        print("Ziņojums NAV DERĪGS!")

if __name__ == "__main__":
    main()