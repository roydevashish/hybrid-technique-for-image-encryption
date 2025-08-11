import os
from dotenv import load_dotenv
load_dotenv()

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def get_adjacent_pixel_pairs(pixel_array, direction):
	height, width = pixel_array.shape
	if direction == 'horizontal':
		x_pixels = pixel_array[:, :-1].flatten()
		y_pixels = pixel_array[:, 1:].flatten()
	elif direction == 'vertical':
		x_pixels = pixel_array[:-1, :].flatten()
		y_pixels = pixel_array[1:, :].flatten()
	elif direction == 'diagonal':
		x_pixels = pixel_array[:-1, :-1].flatten()
		y_pixels = pixel_array[1:, 1:].flatten()
	else:
		raise ValueError("Invalid direction")
	return x_pixels, y_pixels


def plot_rgb_correlation_graph(image_path):
	file_name = image_path.split("/")[-1]
	
	# Load RGB image
	img = Image.open(image_path).convert('RGB')
	pixel_array = np.array(img, dtype=np.float64)

	directions = ['horizontal', 'vertical', 'diagonal']
	channels = ['Red', 'Green', 'Blue']

	plt.figure(figsize=(18, 12))

	plot_idx = 1
	for direction in directions:
		for i, channel in enumerate(channels):
			channel_data = pixel_array[:, :, i]
			x, y = get_adjacent_pixel_pairs(channel_data, direction)

			plt.subplot(3, 3, plot_idx)
			plt.scatter(
				x, y,
				s=1,            					# Small dot size for dotted effect
				alpha=0.5,        				# Slight transparency for better visuals
				color=channel.lower(),
				edgecolors='none' 				# Ensures clean dots without edges
			)
			plt.xlabel(f'Pixel value ({channel})')
			plt.ylabel(f'Adjacent pixel ({direction})')
			plt.title(f'{channel} Channel - {direction.capitalize()} Correlation')
			plt.grid(True)
			plot_idx += 1

	plt.tight_layout()
	rgb_correlation_graph_path = os.path.join(os.getenv("ANALYSIS_DIR"), "correlation_graph", "rgb", f"{file_name}.png")
	plt.savefig(rgb_correlation_graph_path)
	plt.close()

	img = img.convert("L")
	pixel_array = np.array(img, dtype=np.float64)

	plt.figure(figsize=(15, 5))
	for i, direction in enumerate(directions, 1):
		x, y = get_adjacent_pixel_pairs(pixel_array, direction)
		plt.subplot(1, 3, i)
		plt.scatter(x, y, s=1, alpha=0.5)
		plt.xlabel('Current pixel value')
		plt.ylabel('Adjacent pixel value')
		plt.title(f'{direction.capitalize()} Correlation')
		plt.grid(True)

	plt.tight_layout()
	grayscale_correlation_graph_path = os.path.join(os.getenv("ANALYSIS_DIR"), "correlation_graph", "grayscale", f"{file_name}.png")
	plt.savefig(grayscale_correlation_graph_path)
	plt.close()


def CorrelationGraph():
	encrypted_img_dir = os.getenv("IMG_ENCRYPTED")

	for file in os.listdir(encrypted_img_dir):
		encrypted_img_path = os.path.join(encrypted_img_dir, file)

		if os.path.isfile(encrypted_img_path) and file != ".DS_Store":
			print(f"Processing image: {encrypted_img_path}")
			plot_rgb_correlation_graph(encrypted_img_path)
