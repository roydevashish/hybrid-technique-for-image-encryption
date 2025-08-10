import os
from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import numpy as np

def CalculateUACIPixelWise(img1_path, img2_path):
  img1 = Image.open(img1_path).convert("RGB")
  img2 = Image.open(img2_path).convert("RGB")
  width, height = img1.size

  img1_array = np.array(img1, dtype=np.float64)
  img2_array = np.array(img2, dtype=np.float64)

  sum_of_abs_diff = np.sum(abs(img1_array - img2_array))
  uaci = (sum_of_abs_diff * 100) / (255 * height * width)
  return uaci


def CalculateUACIChannelWise(original_encrypted, modified_encrypted):
  img1 = Image.open(original_encrypted).convert("RGB")
  img2 = Image.open(modified_encrypted).convert("RGB")

  # Convert to numpy arrays
  array1 = np.array(img1, dtype=np.float64)
  array2 = np.array(img2, dtype=np.float64)
  
  # Calculate absolute differences
  diff = np.abs(array1 - array2)
  sum_of_diff = np.sum(diff)
  
  # Calculate UACI
  width, height = img1.size
  channels = 3  # RGB
  uaci = sum_of_diff / (255 * width * height * channels) * 100
  return uaci


def UACI():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  original_encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
  modified_encrypted_img_dir = os.getenv("IMG_ENCRYPTED_FOR_NPCR")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  uaci_file = open(os.path.join(analysis_dir, "uaci.csv"), "a")

  for file in os.listdir(original_img_dir):
    original_img_path = os.path.join(original_img_dir, file)
    original_encrypted_img_path = os.path.join(original_encrypted_img_dir, file)
    modified_encrypted_img_path = os.path.join(modified_encrypted_img_dir, file)

    if os.path.isfile(original_img_path) and file != ".DS_Store":
      print(f"Processing image: {original_img_path}")
      uaci = CalculateUACIPixelWise(original_encrypted_img_path, modified_encrypted_img_path)
      uaci1 = CalculateUACIChannelWise(original_encrypted_img_path, modified_encrypted_img_path)
      
      uaci_file_string = f"{file}|{uaci}|{uaci1}\n"
      uaci_file.write(uaci_file_string)

  uaci_file.close()
