from PIL import Image

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