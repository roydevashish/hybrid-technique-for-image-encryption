from src.analysis.entropy import Entropy
from src.analysis.npcr import NPCR

def Analysis():
  print("Starting Analysis...")

  # 1. Time Series

  # 2. Entropy of image
  print(f"Calculating Entropy...")
  Entropy()
  print(f"Entropy Calculated...")
  print()

  # 3. Correlation cofficient

  # 4. MSE
  
  # 5. NPCR
  print(f"Calculating NPCR...")
  NPCR()
  print(f"NPCR Calculated...")
  print()
  
  # 6. UACI
  
  # 7. NIST Test (optional)

  print("Analysis Completed...")
