from processor.sp import _fix_sp_processor
from fastai.text import load_learner
from dotenv import load_dotenv
import os
from pathlib import Path
import gdown
import os

load_dotenv()
# one hot encoder
gdown.download("https://drive.google.com/uc?id=1-1K0jcHICzjgcaY64UeLC_PuEN5tI_Xa")
os.rename("./onehot.pkl", "./artifacts/onehot.pkl")

# spm model
gdown.download("https://drive.google.com/uc?id=1CyT0AI_PdWDZrnful6jBXFqAOfTrIOSe")
os.rename("./spm.model", "./artifacts/spm.model")

# spm vocab
gdown.download("https://drive.google.com/uc?id=1bGetu3Uzq06OrtdvVmRfiY6uorVSayIS")
os.rename("./spm.vocab", "./artifacts/spm.vocab")

# trained_model_fp32_fwd_classifier
gdown.download("https://drive.google.com/uc?id=1R6Mm_K2ARMjNEuTikMmpHO0goggh0Rg9")
os.rename(
    "./trained_model_fp32_fwd_classifier.pkl",
    "./artifacts/trained_model_fp32_fwd_classifier.pkl",
)

artifactsPath = Path(os.getenv("artifactsPath"))
modelFileName = os.getenv("modelFileName")
spModel = os.getenv("spmodelFileName")
spVocab = os.getenv("spmodelVocabFileName")

model = load_learner(artifactsPath, modelFileName)
_fix_sp_processor(model, artifactsPath, spModel, spVocab)
