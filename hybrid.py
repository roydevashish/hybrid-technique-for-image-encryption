import image as Img
import matrix as Matrix
import chacha20 as ChaCha20

import os
from dotenv import load_dotenv

load_dotenv()

def encryption(img):
    input_dir = os.getenv("INPUT_DIR")
    output_dir = os.getenv("OUTPUT_DIR")
    chacha20_key = os.getenv("CHACHA20_KEY")

    # image changed to matrix
    raw_hex_matrix = Img.img_to_hex(f"{input_dir}/{img}")

    # matrix is changed to string
    matrix_in_string_formate = Matrix.matrix_to_string(raw_hex_matrix)

    # matrix string is encrypted using chacha20
    enc_matrix_in_string_formate, nonce = ChaCha20.encryption(matrix_in_string_formate, chacha20_key)

    # string is changed back to matrix
    enc_hex_matrix = Matrix.string_to_matrix(enc_matrix_in_string_formate, raw_hex_matrix)

    # matrix is changed to image and saved to output folder
    Img.hex_to_img(enc_hex_matrix, f"{output_dir}/{nonce}-{img}")

def decryption():
    pass