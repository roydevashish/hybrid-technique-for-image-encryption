import os
from dotenv import load_dotenv
load_dotenv()

import math
from skimage import io
from collections import Counter

def CalculateEntropy(img_path):
  img_array = io.imread(img_path)

  def entropy(channel_data):
    flat = channel_data.flatten()
    counts = Counter(flat)
    total = len(flat)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

  if img_array.ndim == 2:  # Grayscale image
    ent = entropy(img_array)
    return ent, ent, ent, ent
  elif img_array.ndim == 3 and img_array.shape[2] == 3:  # RGB image
    r_ent = entropy(img_array[:, :, 0])
    g_ent = entropy(img_array[:, :, 1])
    b_ent = entropy(img_array[:, :, 2])
    avg_ent = (r_ent + g_ent + b_ent) / 3
    return r_ent, g_ent, b_ent, avg_ent
  else:
    raise ValueError("Unsupported image format")
  

def Entropy():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
  decrypted_img_dir = os.getenv("IMG_DECRYPTED")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  entropy_file = open(os.path.join(analysis_dir, "entropy.csv"), "a")

  for file in os.listdir(original_img_dir):
    input_img_path = os.path.join(original_img_dir, file)
    encrypted_img_path = os.path.join(encrypted_img_dir, file)
    decrypted_img_path = os.path.join(decrypted_img_dir, file)

    if os.path.isfile(input_img_path) and file != ".DS_Store":
      path_list = [input_img_path, encrypted_img_path, decrypted_img_path]
      
      entropy_file_string = f"{file}|"

      for each_path in path_list:
        red_entropy, green_entropy, blue_entropy, avg_entropy = CalculateEntropy(each_path)
        entropy_file_string += f"{red_entropy}|{green_entropy}|{blue_entropy}|{avg_entropy}|"
      
      entropy_file_string += "\n"
      entropy_file.write(entropy_file_string)

  entropy_file.close()
