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
            print(str(idx) + " & \includegraphics[width=0.6\\textwidth]{assets/histogram/" + file + "}\\\\ \hline")
            # print(str(idx) +"\\ref{img:" + file + "} & \includegraphics[width=0.1\\textwidth]{assets/original/" + file + "} & \includegraphics[width=0.1\\textwidth]{assets/encrypted/" + file + "} & \includegraphics[width=0.1\\textwidth]{assets/decrypted/" + file + "}\\\\ \hline")

            # print(str(idx) + " & " + file + " & \includegraphics[width=0.1\\textwidth]{assets/original/" + file + "} & 512x512\\\\ \hline")
            idx += 1
            
        continue 

        input_img_path = os.path.join(original_img_dir, file)
        encrypted_img_path = os.path.join(encrypted_img_dir, file)
        decrypted_img_path = os.path.join(decrypted_img_dir, file)
        
        if os.path.isfile(input_img_path) and file != ".DS_Store":
            print(f"Starting processing file: {file}")
            print(f"{input_img_path} -> {encrypted_img_path} -> {decrypted_img_path}")

            # Hybrid.encryption(input_img_path, encrypted_img_path, decrypted_img_path)

            print(f"Processing completed.")
            print()