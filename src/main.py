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

      # enc_time_file = open("data/results/hybrid_enc_dec_time.csv", "a")
      # enc_start_time = time.time() 

      Hybrid.encryption(input_img_path, encrypted_img_path)

      # enc_end_time = time.time()
      # enc_execution_time = enc_end_time - enc_start_time

      # dec_start_time = time.time() 

      Hybrid.decryption(encrypted_img_path, decrypted_img_path)
  
      # dec_end_time = time.time()
      # dec_execution_time = dec_end_time - dec_start_time

      # enc_time_file_string = f"{original_img}|{enc_execution_time}|{dec_execution_time} \n"
      # enc_time_file.write(enc_time_file_string)
      # enc_time_file.close()

      print(f"Processing Completed.")
      print()