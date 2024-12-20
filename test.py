from PIL import Image
import numpy as np

def image_to_hex_matrix(image_path):
    """
    Processes the input image, converts it to a matrix where each cell
    contains the RGB values of the pixel, and represents the pixel data in hex.

    Args:
        image_path (str): Path to the JPEG/JPG image file.

    Returns:
        tuple: A tuple containing the hex matrix and RGB matrix.
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

def hex_matrix_to_image(hex_matrix, output_path):
    """
    Converts a hex matrix back into an image and saves it to the specified path.

    Args:
        hex_matrix (list): A 2D list of hex color codes.
        output_path (str): Path to save the generated image.
    """
    try:
        # Determine the dimensions of the matrix
        height = len(hex_matrix)
        width = len(hex_matrix[0]) if height > 0 else 0

        # Create an image
        img = Image.new("RGB", (width, height))

        # Populate the image with pixel data
        for y, row in enumerate(hex_matrix):
            for x, hex_color in enumerate(row):
                # Convert hex color to RGB tuple
                r = int(hex_color[0:2], 16)
                g = int(hex_color[2:4], 16)
                b = int(hex_color[4:6], 16)
                img.putpixel((x, y), (r, g, b))

        # Save the image
        img.save(output_path)
        print(f"Image saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input image path
    image_path = input("Enter the path to the JPEG/JPG image file: ").strip()

    # Process the image
    hex_matrix = image_to_hex_matrix(image_path)



    if hex_matrix:
        # print("\nHex Matrix:")
        # for row in hex_matrix:
        #     print(row)

        # Convert the hex matrix back to an image
        # output_path = input("Enter the path to save the generated image: ").strip()
        output_path = image_path
        hex_matrix_to_image(hex_matrix, output_path)
