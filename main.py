import image_manipulation as IM
import matrix_manipulation as Matrix
import chacha20 as ChaCha20

def encryption(input_img_path = None, key = None, output_img_path = None, key_management_filename = None):
    # take the path of input image.
    if input_img_path == None:
        input_img_path = input("Path of input image: ")
    
    # change the image to hex code matrix
    img_hex_matrix = IM.img_to_hex(input_img_path)
    
    # change the matrix to string
    plaintext = Matrix.matrix_to_string(img_hex_matrix)

    # take the key for encryption
    if key == None:
        key = input("Input key for encryption (64 hex code i.e. 256bit): ")

    # do the proper encryption
    ciphertext, nonce = ChaCha20.encryption(plaintext, key)
    
    # print the nonce value for further decryption
    # print(f"Nonce value for this encryption: {nonce}")

    # change the string to matrix
    img_hex_matrix = Matrix.string_to_matrix(ciphertext, img_hex_matrix)
    
    # take the path for output image
    if output_img_path == None:
        output_img_path = input("Path for output image: ")

    # change the hex code matrix to image
    # and save the image to the output folder.
    IM.hex_to_img(img_hex_matrix, output_img_path)

    # save the details of encryption in a file for further decryption process
    if key_management_filename == None:
        key_management_filename = "key_details.csv"
    key_management_file = open("key_management/" + key_management_filename, "a")
    key_management_file.write(f"{input_img_path}|{key}|{nonce}|{output_img_path} \n")
    key_management_file.close()

def decryption(input_img_path = None, key = None, nonce = None, output_img_path = None):
    # take the path of input image.
    if input_img_path == None:
        input_img_path = input("Path of input image: ")
    
    # change the image to hex code matrix
    img_hex_matrix = IM.img_to_hex(input_img_path)
    
    # change the matrix to string
    ciphertext = Matrix.matrix_to_string(img_hex_matrix)
    
    # take the key and nonce value for decryption
    if key == None:
        key = input("Input key for decryption (64 hex code i.e. 256bit): ")
    if nonce == None:
        nonce = input("Input nonce for the decryption: ")

    # do the proper decryption
    plaintext = ChaCha20.decryption(ciphertext, key, nonce)

    # change the string to matrix
    img_hex_matrix = Matrix.string_to_matrix(plaintext, img_hex_matrix)

    # take the path for output image
    if output_img_path == None:
        output_img_path = input("Path for output image: ")

    # change the hex code matrix to image
    # and save the image to the output folder. 
    IM.hex_to_img(img_hex_matrix, output_img_path)

def main():
    # print the menu
    print("Menu: ")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    # take the option from the user
    menu_option = int(input("Select from the menu: "))

    # execute the operation accourding to the user's selection
    if(menu_option == 1):
        encryption()
        exit
    elif(menu_option == 2):
        decryption()    
        exit
    elif(menu_option == 3):
        return

if __name__ == "__main__":
    main()