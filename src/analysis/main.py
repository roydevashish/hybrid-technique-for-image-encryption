from src.analysis.entropy import Entropy
from src.analysis.npcr import NPCR
from src.analysis.mse import MSE
from src.analysis.uaci import UACI
from src.analysis.correlationCofficient import CorrelationCofficient

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

  print("Analysis Completed...")
