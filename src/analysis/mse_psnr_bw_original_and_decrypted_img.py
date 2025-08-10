import os
from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import numpy as np
import math

def CalculateMSEAndPSNR(img1_path, img2_path):
  img1 = np.array(Image.open(img1_path).convert("RGB"), dtype=np.float64)
  img2 = np.array(Image.open(img2_path).convert("RGB"), dtype=np.float64)

  mse = np.mean((img1 - img2) ** 2)
  if(mse == 0):
    return 0, float("inf")
  
  psnr = 10 * math.log10((255.0 ** 2) / mse)
  return mse, psnr


def MSEAndPSNRBetweenOriginalAndDecryptedImage():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  decrypted_img_dir = os.getenv("IMG_DECRYPTED")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  mse_psnr_file = open(os.path.join(analysis_dir, "mse_psnr_bw_original_and_decrypted_img.csv"), "a")

  for file in os.listdir(original_img_dir):
    original_img_path = os.path.join(original_img_dir, file)
    decrypted_img_path = os.path.join(decrypted_img_dir, file)
    
    if os.path.isfile(original_img_path) and file != ".DS_Store":
      print(f"Processing image: {original_img_path}")
      
      mse, psnr = CalculateMSEAndPSNR(original_img_path, decrypted_img_path)

      mse_psnr_file_string = f"{file}|{mse}|{psnr}\n"
      mse_psnr_file.write(mse_psnr_file_string)
      
  mse_psnr_file.close()
