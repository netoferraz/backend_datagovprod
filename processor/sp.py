from fastai.text import SPProcessor
from fastai.basic_train import Learner
from pathlib import Path


def _fix_sp_processor(
    learner: Learner, sp_path: Path, sp_model: str, sp_vocab: str
) -> None:
    """
    Fixes SentencePiece paths serialized into the model.
    Parameters
    ----------
    learner
        Learner object
    sp_path
        path to the directory containing the SentencePiece model and vocabulary files.
    sp_model
        SentencePiece model filename.
    sp_vocab
        SentencePiece vocabulary filename.
    """
    for processor in learner.data.processor:
        if isinstance(processor, SPProcessor):
            processor.sp_model = sp_path / sp_model
            processor.sp_vocab = sp_path / sp_vocab
