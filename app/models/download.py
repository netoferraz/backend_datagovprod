import gdown
import os
artifactsPath = './artifacts'
if not os.path.exists(artifactsPath):
    os.makedirs(artifactsPath)
# one hot encoder
if not os.path.isfile("./artifacts/onehot.pkl"):
    gdown.download("https://drive.google.com/uc?id=1-1K0jcHICzjgcaY64UeLC_PuEN5tI_Xa")
    os.rename("./onehot.pkl", "./artifacts/onehot.pkl")

# spm model
if not os.path.isfile("./artifacts/spm.model"):
    gdown.download("https://drive.google.com/uc?id=1CyT0AI_PdWDZrnful6jBXFqAOfTrIOSe")
    os.rename("./spm.model", "./artifacts/spm.model")

# spm vocab
if not os.path.isfile("./artifacts/spm.vocab"):
    gdown.download("https://drive.google.com/uc?id=1bGetu3Uzq06OrtdvVmRfiY6uorVSayIS")
    os.rename("./spm.vocab", "./artifacts/spm.vocab")

# trained_model_fp32_fwd_classifier
if not os.path.isfile("./artifacts/trained_model_fp32_fwd_classifier.pkl"):
    gdown.download("https://drive.google.com/uc?id=1R6Mm_K2ARMjNEuTikMmpHO0goggh0Rg9")
    os.rename(
        "./trained_model_fp32_fwd_classifier.pkl",
        "./artifacts/trained_model_fp32_fwd_classifier.pkl",
    )
