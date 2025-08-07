import os
from dotenv import load_dotenv
load_dotenv()

import src.app.image as IMG
import numpy as np
from skimage import io
import math

def ClaculateMSE(img1_path, img2_path, croped_img_path):
  img1_hex_matrix = IMG.img_to_hex(img1_path)
  img2_hex_matrix = IMG.img_to_hex(img2_path)
  np_img2_hex_matrix = np.array(img2_hex_matrix)
      
  img1 = io.imread(img1_path)

  mse_list = []
  psnr_list = []
  
  for i in range(len(img2_hex_matrix) - len(img1_hex_matrix)):
    for j in range(len(img2_hex_matrix[0]) - len(img1_hex_matrix[0])):
      IMG.hex_to_img(np_img2_hex_matrix[i:i+len(img1_hex_matrix), j:j+len(img1_hex_matrix[0])], croped_img_path)
      img2 = io.imread(croped_img_path)

      mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
      if mse == 0:
        mse_list.append(0)
        psnr_list.append(float("inf"))
        break

      psnr = 10 * math.log10((255.0 ** 2) / mse)
      mse_list.append(mse)
      psnr_list.append(psnr)

  return np.mean(mse_list), np.mean(psnr_list)


def MSE():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
  croped_encrypted_img_dir = os.getenv("CROPED_ENCRYPTED_IMG")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  mse_psnr_file = open(os.path.join(analysis_dir, "mse_psnr.csv"), "a")

  for file in os.listdir(original_img_dir):
    original_img_path = os.path.join(original_img_dir, file)
    encrypted_img_path = os.path.join(encrypted_img_dir, file)
    croped_encrypted_img_path = os.path.join(croped_encrypted_img_dir, file)

    if os.path.isfile(original_img_path) and file != ".DS_Store":
      img = io.imread(original_img_path)
      if(img.ndim == 3):
        print(f"Processing file: {original_img_path}")

        mse, psnr = ClaculateMSE(original_img_path, encrypted_img_path, croped_encrypted_img_path)
      
        mse_psnr_file_string = f"{file}|{mse}|{psnr}\n"
        mse_psnr_file.write(mse_psnr_file_string)

  mse_psnr_file.close()
