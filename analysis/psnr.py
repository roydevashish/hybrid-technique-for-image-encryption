from math import log10, sqrt 
import cv2 
import numpy as np 
import os
from dotenv import load_dotenv
load_dotenv()

def PSNR(original, compressed): 
	mse = np.mean((original - compressed) ** 2) 
	if(mse == 0): # MSE is zero means no noise is present in the signal .  # Therefore PSNR have no importance. 
		mse = 0.1
	max_pixel = 255.0
	psnr = 20 * log10(max_pixel / sqrt(mse)) 
	return psnr 

def main(): 
	original_img_dir = "data/original"
	encrypted_img_dir = "data/decrypted"

	psnr_file = open("data/results/psnr-new.csv", "w")

	idx = 1
	for file in os.listdir(original_img_dir):
		if(file == ".DS_Store"):
			continue

		original = cv2.imread(f"{original_img_dir}/{file}") 
		encrypted = cv2.imread(f"{encrypted_img_dir}/{file}", 1) 
		# original = cv2.resize(original, (encrypted.shape[1], encrypted.shape[0])) 
		value = PSNR(original, encrypted) 

		psnr_file_string = f"{file} & {value} \\\\ \hline"
		psnr_file.write(psnr_file_string + "\n")

		print(f"Processing: {file}")
		print(f"PSNR value is {value} dB") 
		print()
		idx += 1
	
	psnr_file.close()

if __name__ == "__main__": 
	main()