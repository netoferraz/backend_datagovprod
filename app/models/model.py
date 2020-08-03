from processor.sp import _fix_sp_processor
from fastai.text import load_learner
from dotenv import load_dotenv
import os
from pathlib import Path
import gdown
import os

load_dotenv()

artifactsPath = Path(os.getenv("artifactsPath"))
modelFileName = os.getenv("modelFileName")
spModel = os.getenv("spmodelFileName")
spVocab = os.getenv("spmodelVocabFileName")

model = load_learner(artifactsPath, modelFileName)
_fix_sp_processor(model, artifactsPath, spModel, spVocab)
