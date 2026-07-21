import hashlib
from Crypto.Hash import keccak


def generate_md5(text):
    return hashlib.md5(text.encode()).hexdigest()


def generate_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


def generate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()


def generate_keccak(text):
    k = keccak.new(digest_bits=256)
    k.update(text.encode())
    return k.hexdigest()


text = input("Enter your text: ")

print("\n========== HASH GENERATOR ==========\n")

print("MD5 Hash      :", generate_md5(text))
print("SHA1 Hash     :", generate_sha1(text))
print("SHA256 Hash   :", generate_sha256(text))
print("Keccak-256    :", generate_keccak(text))

print("\n====================================")