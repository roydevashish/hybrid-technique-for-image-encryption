from src.analysis.entropy import Entropy
from src.analysis.npcr import NPCR
from src.analysis.mse import MSE
from src.analysis.uaci import UACI
from src.analysis.correlationCofficient import CorrelationCofficient
from src.analysis.histogram import Histogram
from src.analysis.mse_psnr_bw_original_and_decrypted_img import MSEAndPSNRBetweenOriginalAndDecryptedImage
from src.analysis.correlationGraph import CorrelationGraph

def Analysis():
  print("Starting Analysis...")

  # 1. Time Series

  # 2. Entropy of image
  print(f"Calculating Entropy...")
  Entropy()
  print(f"Entropy Calculated...")
  print()

  # 3. Correlation cofficient
  print(f"Calculating correlation cofficient...")
  CorrelationCofficient()
  print(f"Correlation cofficient Calculated...")
  print()

  # 4. MSE and PSNR
  print(f"Calculating MSE and PSNR...")
  MSE()
  print(f"MSE and PSNR Calculated...")
  print()
  
  # 5. NPCR
  print(f"Calculating NPCR...")
  NPCR()
  print(f"NPCR Calculated...")
  print()
  
  # 6. UACI
  print(f"Calculating UACI...")
  UACI()
  print(f"UACI Calculated...")
  print()
  
  # 7. NIST Test (optional)

  # 8. Histogram
  print(f"Calculating Histogram...")
  Histogram()
  print(f"Histogram Calculated...")
  print()

  # 9. MSE and PSNR between original and decrypted image
  print(f"Calculating MSE and PSNR b/w original and decrypted image...")
  MSEAndPSNRBetweenOriginalAndDecryptedImage()
  print(f"MSE and PSNR b/w original and decrypted image Calculated...")
  print()

  # 10. Correlation Graph
  print(f"Calculating correlation graph...")
  CorrelationGraph()
  print(f"Correlation graph calculated...")
  print()

  print("Analysis Completed...")
