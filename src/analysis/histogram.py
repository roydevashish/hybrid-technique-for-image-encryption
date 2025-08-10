import os
from dotenv import load_dotenv
load_dotenv()

import matplotlib.pyplot as plt
from skimage import io

def MakeHistogram(img_path, output_path):
  # Load the sample image
  img = io.imread(img_path)
  
  if(img.ndim == 3):
    #Color image
    # Assuming encrypted_img is your encrypted RGB image (shape: H x W x 3)
    # Split the encrypted image into R, G, B channels
    r_enc = img[:, :, 0]
    g_enc = img[:, :, 1]
    b_enc = img[:, :, 2]

    # Create subplots for each channel
    plt.figure(figsize=(15, 4))

    # Red channel histogram
    plt.subplot(1, 3, 1)
    plt.hist(r_enc.ravel(), bins=256, range=[0, 256], color='red')
    plt.title("Red Channel")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.grid(True)

    # Green channel histogram
    plt.subplot(1, 3, 2)
    plt.hist(g_enc.ravel(), bins=256, range=[0, 256], color='green')
    plt.title("Green Channel")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.grid(True)

    # Blue channel histogram
    plt.subplot(1, 3, 3)
    plt.hist(b_enc.ravel(), bins=256, range=[0, 256], color='blue')
    plt.title("Blue Channel")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(output_path)
  else:
    #Grayscale image
    plt.hist(img.ravel(), bins=256, range=[0, 256], color='blue')
    plt.title("Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.savefig(output_path)
  plt.close()
      

def Histogram():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
  decrypted_img_dir = os.getenv("IMG_DECRYPTED")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  for file in os.listdir(original_img_dir):
    original_img_path = os.path.join(original_img_dir, file)
    encrypted_img_path = os.path.join(encrypted_img_dir, file)
    decrypted_img_path = os.path.join(decrypted_img_dir, file)
    histogram_original_output_path = os.path.join(analysis_dir, "histogram/original", f"{file}.png")
    histogram_encrypted_output_path = os.path.join(analysis_dir, "histogram/encrypted", f"{file}.png")
    histogram_decrypted_output_path = os.path.join(analysis_dir, "histogram/decrypted", f"{file}.png")
    
    if os.path.isfile(original_img_path) and file != ".DS_Store":
      print(f"Processing image: {file}")
      MakeHistogram(original_img_path, histogram_original_output_path)
      MakeHistogram(encrypted_img_path, histogram_encrypted_output_path)
      MakeHistogram(decrypted_img_path, histogram_decrypted_output_path)
