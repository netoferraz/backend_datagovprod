from inference.predict import predict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Tuple

app = FastAPI()


class Ementa(BaseModel):
    ementa: str


class Tags(BaseModel):
    tags: Tuple[str, ...]


@app.post("/predict", response_model=Tags, status_code=200)
def get_prediction(Ementa: Ementa):
    ementa = Ementa.ementa

    predictions = predict(ementa)

    if not predictions:
        raise HTTPException(
            status_code=404, detail="Não foi possível encontrar nenhuma tag apropriada."
        )

    if predictions:
        return {"tags": predictions}
