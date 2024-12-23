from Crypto.Cipher import ChaCha20
from binascii import unhexlify

def encryption(plaintext, key):
    plaintext = unhexlify(plaintext)
    key = unhexlify(key)

    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(plaintext)
    nonce = cipher.nonce
    
    return ciphertext.hex(), nonce.hex()

def decryption(ciphertext, key, nonce):
    ciphertext = unhexlify(ciphertext)
    key = unhexlify(key)
    nonce = unhexlify(nonce)

    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    
    return plaintext.hex()