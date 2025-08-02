import os
from dotenv import load_dotenv
load_dotenv()

from Crypto.Cipher import ChaCha20
from binascii import unhexlify

def encryption(plaintext, key=os.getenv("CHACHA20_KEY"), nonce=os.getenv("CHACHA20_NONCE")):
	plaintext = unhexlify(plaintext)
	key = unhexlify(key)
	nonce = unhexlify(nonce)

	cipher = ChaCha20.new(key=key, nonce=nonce)
	ciphertext = cipher.encrypt(plaintext)
	
	return ciphertext.hex()


def decryption(ciphertext, key=os.getenv("CHACHA20_KEY"), nonce=os.getenv("CHACHA20_NONCE")):
	ciphertext = unhexlify(ciphertext)
	key = unhexlify(key)
	nonce = unhexlify(nonce)

	cipher = ChaCha20.new(key=key, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)
	
	return plaintext.hex()
