import os
from dotenv import load_dotenv
load_dotenv()

import numpy as np
from PIL import Image

def calculate_correlation_coefficient(image_path, direction='all'):
  """
  Calculate correlation coefficient between adjacent pixels
  
  Args:
    image_path: Path to the image file
    direction: 'horizontal', 'vertical', 'diagonal', or 'all'
  
  Returns:
    Dictionary with correlation coefficients for each direction
  """
  try:
    # Load image and convert to grayscale for correlation analysis
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    pixel_array = np.array(img, dtype=np.float64)
    
    height, width = pixel_array.shape
    results = {}
    
    # Calculate horizontal correlation
    if direction in ['horizontal', 'all']:
      results['horizontal'] = _calculate_horizontal_correlation(pixel_array)
    
    # Calculate vertical correlation
    if direction in ['vertical', 'all']:
      results['vertical'] = _calculate_vertical_correlation(pixel_array)
    
    # Calculate diagonal correlation
    if direction in ['diagonal', 'all']:
      results['diagonal'] = _calculate_diagonal_correlation(pixel_array)
    
    return results
      
  except Exception as e:
    print(f"Error calculating correlation: {e}")
    return None


def _calculate_horizontal_correlation(pixel_array):
  """Calculate correlation between horizontally adjacent pixels"""
  height, width = pixel_array.shape
  
  # Get adjacent pixel pairs (current and right neighbor)
  x_pixels = pixel_array[:, :-1].flatten()  # All pixels except last column
  y_pixels = pixel_array[:, 1:].flatten()   # All pixels except first column
  
  return _correlation_formula(x_pixels, y_pixels)


def _calculate_vertical_correlation(pixel_array):
  """Calculate correlation between vertically adjacent pixels"""
  height, width = pixel_array.shape
  
  # Get adjacent pixel pairs (current and bottom neighbor)
  x_pixels = pixel_array[:-1, :].flatten()  # All pixels except last row
  y_pixels = pixel_array[1:, :].flatten()   # All pixels except first row
  
  return _correlation_formula(x_pixels, y_pixels)


def _calculate_diagonal_correlation(pixel_array):
  """Calculate correlation between diagonally adjacent pixels"""
  height, width = pixel_array.shape
  
  # Get diagonal adjacent pixel pairs (current and bottom-right neighbor)
  x_pixels = pixel_array[:-1, :-1].flatten()  # Exclude last row and column
  y_pixels = pixel_array[1:, 1:].flatten()    # Exclude first row and column
  
  return _correlation_formula(x_pixels, y_pixels)


def _correlation_formula(x_pixels, y_pixels):
  """
  Apply correlation coefficient formula
  CC = Σ(xi - x̄)(yi - ȳ) / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]
  """
  # Calculate means
  x_mean = np.mean(x_pixels)
  y_mean = np.mean(y_pixels)
  
  # Calculate deviations from mean
  x_dev = x_pixels - x_mean
  y_dev = y_pixels - y_mean
  
  # Calculate correlation coefficient
  numerator = np.sum(x_dev * y_dev)
  denominator = np.sqrt(np.sum(x_dev**2) * np.sum(y_dev**2))
  
  # Avoid division by zero
  if denominator == 0:
    return 0.0
  
  return numerator / denominator


def calculate_correlation_coefficient_rgb(image_path):
  """Calculate correlation coefficient for each RGB channel"""
  try:
    img = Image.open(image_path).convert('RGB')
    pixel_array = np.array(img, dtype=np.float64)
    
    results = {}
    channels = ['Red', 'Green', 'Blue']
    
    for i, channel in enumerate(channels):
      channel_data = pixel_array[:, :, i]
      
      results[channel] = {
        'horizontal': _calculate_horizontal_correlation(channel_data),
        'vertical': _calculate_vertical_correlation(channel_data),
        'diagonal': _calculate_diagonal_correlation(channel_data)
      }
    
    return results
      
  except Exception as e:
    print(f"Error calculating RGB correlation: {e}")
    return None


def CorrelationCofficient():
  original_img_dir = os.getenv("IMG_ORIGINAL")
  original_encrypted_img_dir = os.getenv("IMG_ENCRYPTED")
  analysis_dir = os.getenv("ANALYSIS_DIR")

  correlation_cofficient_file = open(os.path.join(analysis_dir, "correlation_cofficient.csv"), "a")

  for file in os.listdir(original_img_dir):
    original_img_path = os.path.join(original_img_dir, file)
    encrypted_img_path = os.path.join(original_encrypted_img_dir, file)

    if os.path.isfile(original_img_path) and file != ".DS_Store":
      print(f"Processing image: {encrypted_img_path}")

      rgb_correlations = calculate_correlation_coefficient_rgb(encrypted_img_path)
      red = f"{rgb_correlations["Red"]["horizontal"]:.6f}|{rgb_correlations["Red"]["vertical"]:.6f}|{rgb_correlations["Red"]["diagonal"]:.6f}"
      green = f"{rgb_correlations["Green"]["horizontal"]:.6f}|{rgb_correlations["Green"]["vertical"]:.6f}|{rgb_correlations["Green"]["diagonal"]:.6f}"
      blue = f"{rgb_correlations["Blue"]["horizontal"]:.6f}|{rgb_correlations["Blue"]["vertical"]:.6f}|{rgb_correlations["Blue"]["diagonal"]:.6f}"

      correlation_cofficient_file_string = f"{file}|{red}|{green}|{blue}\n"
      correlation_cofficient_file.write(correlation_cofficient_file_string)

  correlation_cofficient_file.close()
