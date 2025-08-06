import os
from dotenv import load_dotenv
load_dotenv()

import src.app.image as IMG
import src.app.hybrid as Hybrid
import numpy as np

def ChangeOriginalImage(original_img_path, changed_img_path):
  original_img = IMG.img_to_hex(original_img_path)
  original_hexcode = original_img[0][0]
  reverse_original_hexcode = original_hexcode[::-1]

  if(original_hexcode != reverse_original_hexcode):
    original_img[0][0] = reverse_original_hexcode
  else:
    if(original_hexcode == "000000"):
      original_img[0][0] = "FFFFFF"
    else:
      original_img[0][0] = "000000"

  IMG.hex_to_img(original_img, f"{changed_img_path}")


def CalculateNPCR(img1_path, img2_path):
  img1 = np.array(IMG.img_to_hex(img1_path))
  img2 = np.array(IMG.img_to_hex(img2_path))

  return np.sum(img1 != img2) / img1.size * 100


def NPCR():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  original_for_npcr_img_dir = os.getenv("IMG_ORIGINAL_FOR_NPCR")
  encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
  encrypted_for_npcr_img_dir = os.getenv("IMG_ENCRYPTED_FOR_NPCR")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  npcr_file = open(os.path.join(analysis_dir, "npcr.csv"), "a")

  for file in os.listdir(original_img_dir):
    original_img_path = os.path.join(original_img_dir, file)
    changed_img_path = os.path.join(original_for_npcr_img_dir, file)
    encrypted_img_path = os.path.join(encrypted_img_dir, file)
    encrypted_changed_img_path = os.path.join(encrypted_for_npcr_img_dir, file)

    if os.path.isfile(original_img_path) and file != ".DS_Store":
      ChangeOriginalImage(original_img_path, changed_img_path)
      Hybrid.encryption(changed_img_path, encrypted_changed_img_path)
      npcr = CalculateNPCR(encrypted_img_path, encrypted_changed_img_path)
      
      npcr_file_string = f"{file}|{npcr}\n"
      npcr_file.write(npcr_file_string)

  npcr_file.close()
