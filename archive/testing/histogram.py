import cv2
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def histogram(img_path, save_path):  
    # Ensure the file exists
    if not os.path.exists(img_path):
        print(f"Error: Image not found at {img_path}")
        return

    # Load image 
    imageObj = cv2.imread(img_path) 
    if imageObj is None:
        print(f"Error: Unable to read image {img_path}")
        return

    # Close any open figures before creating new ones
    plt.close('all')

    # Display original image
    plt.figure(figsize=(5, 5))
    plt.axis("off") 
    plt.title("Original Image") 
    plt.imshow(cv2.cvtColor(imageObj, cv2.COLOR_BGR2RGB)) 
    plt.show()
    plt.close()  

    # Get RGB histograms
    blue_hist = cv2.calcHist([imageObj], [0], None, [256], [0, 256]) 
    green_hist = cv2.calcHist([imageObj], [1], None, [256], [0, 256]) 
    red_hist = cv2.calcHist([imageObj], [2], None, [256], [0, 256]) 

    # Create histogram plots
    plt.figure(figsize=(6, 8))

    plt.subplot(3, 1, 1)
    plt.title("Histogram of Blue")
    plt.hist(blue_hist, color="blue")

    plt.subplot(3, 1, 2)
    plt.title("Histogram of Green")
    plt.hist(green_hist, color="green")

    plt.subplot(3, 1, 3)
    plt.title("Histogram of Red")
    plt.hist(red_hist, color="red")

    # Adjust layout
    plt.tight_layout()

    # Ensure save directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save histogram
    plt.savefig(save_path)
    plt.show()
    plt.close()


histogram("data/encrypted/boat.png", "data/boat.png")

# if __name__ == "__main__":
#     original_img_dir = "encrypted/chacha20"
#     save_dir = "results/histogram/chacha20_encryption"

#     # if not original_img_dir:
#     #     print(f"Error: "{} path not set in environment variables.")
#     #     exit()

#     valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")

#     for file in os.listdir(original_img_dir):
#         if file == ".DS_Store" or not file.lower().endswith(valid_extensions):
#             print(f"Skipping non-image file: {file}")
#             continue

#         img_path = os.path.join(original_img_dir, file)
#         save_path = os.path.join(save_dir, file + ".png")
#         histogram(img_path, save_path)