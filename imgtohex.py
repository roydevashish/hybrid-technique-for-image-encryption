from PIL import Image
import numpy as np

def image_to_hex_matrix(image_path):
    """
    Processes the input image, converts it to a matrix where each cell
    contains the RGB values of the pixel, and represents the pixel data in hex.

    Args:
        image_path (str): Path to the JPEG/JPG image file.

    Returns:
        matrix: A matrix containing the hex code of each pixel.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            img = img.convert("RGB")  # Ensure the image is in RGB format

            # Get the width and height of the image
            width, height = img.size

            # Get pixel data
            pixel_data = np.array(img)

            # Create matrices
            hex_matrix = []

            for row in pixel_data:
                hex_row = []
                for pixel in row:
                    r, g, b = pixel
                    hex_row.append(f"{r:02x}{g:02x}{b:02x}")

                hex_matrix.append(hex_row)

            return hex_matrix

    except Exception as e:
        print(f"Error: {e}")
        return None, None
