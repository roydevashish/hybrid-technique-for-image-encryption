import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    original_img_dir = "latex-report/assets/original/"
    encrypted_img_dir = "latex-report/assets/encrypted/"
    decrypted_img_dir = "latex-report/assets/decrypted/"
    idx = 1
    for file in os.listdir(original_img_dir):
        if(file != ".DS_Store"):
            file_name = file.split(".")[0]
            print(str(idx) + " & " + file_name + " & \includegraphics[width=0.1\\textwidth]{assets/original/" + file + "} & 512 x 512 & 10 kb\\\\ \hline")
            print()
            idx += 1