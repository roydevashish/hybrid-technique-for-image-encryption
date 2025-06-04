import os
from dotenv import load_dotenv
load_dotenv()

import hybrid as Hybrid

if __name__ == "__main__":
    original_img_dir = os.getenv("IMG_ORIGINAL")
    encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
    decrypted_img_dir = os.getenv("IMG_DECRYPTED")

    for file in os.listdir(original_img_dir):
        input_img_path = os.path.join(original_img_dir, file)
        encrypted_img_path = os.path.join(encrypted_img_dir, file)
        decrypted_img_path = os.path.join(decrypted_img_dir, file)
        
        if os.path.isfile(input_img_path) and file != ".DS_Store":
            print(f"Starting processing file: {file}")
            print(f"{input_img_path} -> {encrypted_img_path} -> {decrypted_img_path}")

            Hybrid.encryption(input_img_path, encrypted_img_path, decrypted_img_path)

            print(f"Processing completed.")
            print()