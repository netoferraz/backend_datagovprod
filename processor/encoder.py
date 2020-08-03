from dotenv import load_dotenv
from pathlib import Path
import os
import pickle
import warnings

warnings.filterwarnings("ignore")  # "error", "ignore", "always", "default", "module"
load_dotenv()

artifactsPath = Path(os.getenv("artifactsPath"))
mlBinarizerFileName = os.getenv("mlbinarizerFileName")

with open(artifactsPath / mlBinarizerFileName, "rb") as f:
    onehot = pickle.load(f)
