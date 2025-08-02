import os
from dotenv import load_dotenv
load_dotenv()

import random
from ecpy.curves import Curve, Point
from binascii import unhexlify

def message_to_point(curve: Curve, message: bytes) -> Point:
	# Number of bytes to represent a coordinate of a point
	coordinate_size = curve.size // 8
	# Minimum number of bytes for the padding. We need at least 1 byte so that
	# we can try different values and find a valid point. We also add an extra
	# byte as a delimiter between the message and the padding (see below)
	min_padding_size = 2
	# Maximum number of bytes that we can encode
	max_message_size = coordinate_size - min_padding_size

	if len(message) > max_message_size:
		raise ValueError('Message too long')

	# Add a padding long enough to ensure that the resulting padded message has
	# the same size as a point coordinate. Initially the padding is all 0
	padding_size = coordinate_size - len(message)
	padded_message = bytearray(message) + b'\0' * padding_size

	# Put a delimiter between the message and the padding, so that we can
	# properly remove the padding at decrypt time
	padded_message[len(message)] = 0xff

	while True:
		# Convert the padded message to an integer, which may or may not be a
		# valid x-coordinate
		x = int.from_bytes(padded_message, 'little')
		# Calculate the corresponding y-coordinate (if it exists)
		y = curve.y_recover(x)
		if y is None:
			# x was not a valid coordinate; increment the padding and try again
			padded_message[-1] += 1
		else:
			# x was a valid coordinate; return the point (x, y)
			return Point(x, y, curve)


def encrypt(public_key: Point, message: bytes) -> bytes:
	curve = public_key.curve
	# Map the message to an elliptic curve point
	message_point = message_to_point(curve, message)
	# Generate a randon number
	seed = random.randrange(0, curve.field)
	# Calculate c1 and c2 according to the ElGamal algorithm
	c1 = seed * curve.generator
	c2 = seed * public_key + message_point
	# Encode c1 and c2 and return them
	return bytes(curve.encode_point(c1) + curve.encode_point(c2))


def point_to_message(point: Point) -> bytes:
	curve = Curve.get_curve("secp521r1")
	# Number of bytes to represent a coordinate of a point
	coordinate_size = curve.size // 8
	# Convert the x-coordinate of the point to a byte string
	padded_message = point.x.to_bytes(coordinate_size, 'little')
	# Find the padding delimiter
	message_size = padded_message.rfind(0xff)
	# Remove the padding and return the resulting message
	message = padded_message[:message_size]
	return message


def decrypt(curve: Curve, secret_key: int, ciphertext: bytes) -> bytes:
	# Decode c1 and c2 and convert them to elliptic curve points
	c1_bytes = ciphertext[:len(ciphertext) // 2]
	c2_bytes = ciphertext[len(ciphertext) // 2:]
	c1 = curve.decode_point(c1_bytes)
	c2 = curve.decode_point(c2_bytes)

	# Calculate the message point according to the ElGamal algorithm
	message_point = c2 - secret_key * c1
	# Convert the message point to a message and return it
	return point_to_message(message_point)


def encryption(plaintext):
	curve = Curve.get_curve("secp521r1")

	secret_key = int(os.getenv("ECC_PRIVATE_KEY"), 16)
	public_key = secret_key * curve.generator

	range_of_i = (len(plaintext)//126) if len(plaintext) % 126 == 0 else (len(plaintext)//126)+1

	encrypted_string = ""

	for i in range(range_of_i):
		message = plaintext[i*126: i*126 + 126]
		encrypted = encrypt(public_key, unhexlify(message)) + b'\0' * 1
		encrypted_string += encrypted.hex()
	
	return encrypted_string


def decryption(plaintext):
	curve = Curve.get_curve("secp521r1")

	secret_key = int(os.getenv("ECC_PRIVATE_KEY"), 16)
	public_key = secret_key * curve.generator

	range_of_i = len(plaintext) // 534

	decrypted_string = ""

	for i in range(range_of_i):
		message = plaintext[i*534: i*534 + 534]
		decrypted = decrypt(curve, secret_key, unhexlify(message))
		decrypted_string += decrypted.hex()
	
	return decrypted_string
