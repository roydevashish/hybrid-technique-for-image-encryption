from imgtohex import image_to_hex_matrix
from chacha20 import encryption, decryption

from os import urandom

if __name__ == "__main__":
    input_img_path = "input/sample.jpg"
    output_img_path = "output/sample.jpg"

    img_matrix = image_to_hex_matrix(input_img_path)
    key = "f81d2e2288bd230adaaab9e6c84aa7689550fe3d271df579bd9bb6e8a379e1d1"

    plaintext = ""
    for row in img_matrix:
        for col in row:
            plaintext += col

    ciphertext, nonce = encryption(plaintext, key)

    for i in range(0, len(ciphertext), 6):
        print(ciphertext[i: i+6])


    print()