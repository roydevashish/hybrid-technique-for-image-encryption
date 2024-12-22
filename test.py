from imgtohex import image_to_hex_matrix
from hextoimg import hex_matrix_to_image
from chacha20 import encryption, decryption

from os import urandom

if __name__ == "__main__":
    input_img_path = "input/sample-01.jpg"
    output_img_path = "output/sample-01.jpg"

    img_matrix = image_to_hex_matrix(input_img_path)
    key = "f81d2e2288bd230adaaab9e6c84aa7689550fe3d271df579bd9bb6e8a379e1d1"

    plaintext = ""
    for row in img_matrix:
        for col in row:
            plaintext += col

    ciphertext, nonce = encryption(plaintext, key)

    i = 0
    for row in range(len(img_matrix)):
        for col in range(len(img_matrix[row])):
            img_matrix[row][col] = ciphertext[i:i+6]
            i+=6

    hex_matrix_to_image(img_matrix, output_img_path)