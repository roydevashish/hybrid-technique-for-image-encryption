# import required module
import os
from test import encryption_wrapper

# assign directory
input_directory = 'input'

# iterate over files in
# that directory
for filename in os.listdir(input_directory):
	input_img_path = os.path.join(input_directory, filename)
	# checking if it is a file
	if os.path.isfile(input_img_path) and filename != ".DS_Store":
		print(input_img_path)
		output_img_path = "output/" + filename
		encryption_wrapper(input_img_path, output_img_path)
		
