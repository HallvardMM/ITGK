import binascii
import random
 
def to_hex(word):
    return int(str(binascii.hexlify(word), "ascii"), 16)
 
def to_string(word):
    return str(binascii.unhexlify(hex(word)[2:]), "ascii")

def encrypt(message, key):
    message = bytes(message, encoding = "ascii")
    kode1 = to_hex(message)
    key = bytes(key, encoding = "ascii")
    kode2 = to_hex(key)
    krypto = kode1^kode2
    return krypto

def decrypt(krypto, key):
    key = bytes(key, encoding = "ascii")
    kode2 = to_hex(key)
    kode1 = krypto^kode2
    melding = to_string(kode1)
    return melding

def main():
    nøkkel = ""
    melding = str(input("Hva er meldingen? "))
    while len(nøkkel)<len(melding):
        nøkkel = str(nøkkel) + random.choice("abcdefghijklmnopqrstuvwxyz")
    print(nøkkel)
    krypto = encrypt(melding, nøkkel)
    melding2 = decrypt(krypto, nøkkel)
    print("Krypto: " + str(krypto))
    print("Melding: " + str(melding2))

def main2():
    nøkkel = "abcdefghijklmnopqrst"
    melding1 = "hei du er veldig kul"
    melding2 = "hvorfor har du dette"
    print(nøkkel)
    print(melding1)
    print(melding2)
    krypto1 = encrypt(melding1, nøkkel)
    krypto2 = encrypt(melding2, nøkkel)
    message = bytes("hei", encoding = "ascii")
    kode1 = to_hex(message)
    krypto3 = krypto1^krypto2
    krypto_3 = list(str(krypto3))
    kode_1 = list(str(kode1))
    while len(krypto_3) > len(kode_1):
        krypto_3.pop(-1)
    krypto3 = "".join(krypto_3)
    kode2 = kode1^int(krypto3)
    kode3 = to_string(kode2)
    print()
    print(krypto1)
    print(krypto2)
    print(krypto3)
    print(kode1)
    print(kode2)
    print(kode3)

print(encrypt("hei", "abc"))
print(decrypt(591626, "abc"))
main2()
