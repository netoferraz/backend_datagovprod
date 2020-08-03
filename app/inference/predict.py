from models.model import model
from processor.encoder import onehot
from typing import Tuple, Optional
import numpy as np
import warnings

warnings.filterwarnings("ignore")  # "error", "ignore", "always", "default", "module"


def predict(ementa: str) -> Optional[Tuple[str]]:
    """Faz a predição das tags dada uma ementa.

    Parameters
    ----------
    ementa : str
        Ementa

    Returns
    -------
    Optional[Tuple[str]]
        Retorna uma tupla caso há predição, do contrário, None.
    """
    if not isinstance(ementa, str):
        raise TypeError("O parâmetro ementa deve ser uma string")
    p = onehot.inverse_transform(np.atleast_2d(model.predict(ementa)[0].data.numpy()))
    if p:
        return p[0]
    else:
        return None
