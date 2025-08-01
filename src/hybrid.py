import image as Img
import matrix as Matrix
import chacha20 as ChaCha20
import ecc as ECC
import equation as EQU
import padding as PAD

def encryption(original_img, encrypted_img) :
    # Encryption Part Starts
    print("Encryption Started...")

    # Convert img to matrix
    img_matrix = Img.img_to_hex(f"{original_img}")

    # Convert img matrix to string
    img_matrix_string = Matrix.matrix_to_string(img_matrix)

    # Encrypt the img matrix string using ecc
    ecc_enc_img_matrix_string = ECC.encryption(img_matrix_string)

    # Apply padding
    original_img_height = len(img_matrix)
    original_img_width = len(img_matrix[0]) if original_img_height > 0 else 0

    ecc_enc_img_matrix_string_len = len(ecc_enc_img_matrix_string)
    required_no_of_pixel_for_ecc_enc_img_matrix_string = ecc_enc_img_matrix_string_len // 6
    valueofx = EQU.solveforx(original_img_height, original_img_width, required_no_of_pixel_for_ecc_enc_img_matrix_string)

    enc_img_height = original_img_height + valueofx
    enc_img_width = original_img_width + valueofx
    enc_img_pixel = enc_img_height * enc_img_width
    enc_img_blank_pixel = enc_img_pixel - required_no_of_pixel_for_ecc_enc_img_matrix_string
    length_of_padding = enc_img_blank_pixel * 6
    ecc_enc_img_matrix_string_with_padding = PAD.padding(ecc_enc_img_matrix_string, length_of_padding, original_img_height, original_img_width)

    # Encrypt the encrypted img matrix string with padding using chacha20
    chacha20_enc_img_matrix_string = ChaCha20.encryption(ecc_enc_img_matrix_string_with_padding)

    # Construct the new matrix and put the pixel data
    rows, cols = enc_img_height, enc_img_width
    enc_img_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    enc_img_matrix = Matrix.string_to_matrix(chacha20_enc_img_matrix_string, enc_img_matrix)

    # Convert back to img and save it
    Img.hex_to_img(enc_img_matrix, f"{encrypted_img}")

    # Encryption Part Completed
    print("Encryption Completed...")

def decryption(encrypted_img, decrypted_img) :
    # Decryption Part Starts
    print("Decryption Started...")

    # Convert img to matrix
    img_matrix = Img.img_to_hex(f"{encrypted_img}")

    # Convert img matrix to string
    img_matrix_string = Matrix.matrix_to_string(img_matrix)

    # Decrypt the img matrix string using chacha20
    dec_chacha20_img_matrix_string = ChaCha20.decryption(img_matrix_string)

    # Remove padding
    dec_chacha20_img_matrix_string_without_padding, new_img_height, new_img_width = PAD.removepadding(dec_chacha20_img_matrix_string)

    # Decrypt the decrypted img matrix string without padding using ecc
    dec_ecc_img_matrix_string = ECC.decryption(dec_chacha20_img_matrix_string_without_padding)

    # Construct the new matrix and put the pixel data
    rows, cols = new_img_height, new_img_width
    dec_img_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    dec_img_matrix = Matrix.string_to_matrix(dec_ecc_img_matrix_string, dec_img_matrix)

    # Convert back to img and save it
    Img.hex_to_img(dec_img_matrix, f"{decrypted_img}")

    # Decryption Part Completed
    print("Decryption Completed...")