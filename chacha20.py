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























# def decryption(ciphertext, key):
#     plaintext = ciphertext + key
#     return plaintext


# import json
# from base64 import b64encode
# from Crypto.Cipher import ChaCha20
# from Crypto.Random import get_random_bytes

# plaintext = b'\x00\x00\x00'
# key = get_random_bytes(32)
# cipher = ChaCha20.new(key=key)
# ciphertext = cipher.encrypt(plaintext)

# # nonce = b64encode(cipher.nonce).decode('utf-8')
# # ct = b64encode(ciphertext).decode('utf-8')
# # result = json.dumps({'nonce':nonce, 'ciphertext':ct})
# print(ciphertext.hex())

# output_file = open("output.txt", "w")
# output_file.write(str(plaintext.hex()) + "\n")
# output_file.write(str(key.hex()) + "\n")
# output_file.write(str(ciphertext.hex()) + "\n")