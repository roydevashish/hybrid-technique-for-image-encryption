import os
import main as MyAlgo

input_dir = input("Input directory path: ")
output_dir = input("Output directory path: ")
key = input("Input key: ")
key_management_filename = input("Key Details file Name: ")

for file_name in os.listdir(input_dir):
	input_img_path = os.path.join(input_dir, file_name)
	output_img_path = os.path.join(output_dir, file_name)
	if os.path.isfile(input_img_path) and file_name != ".DS_Store":
		MyAlgo.encryption(input_img_path, key, output_img_path, key_management_filename)