from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Project 2 - Template"}


class PredictionInput(BaseModel):
    age: int
    bmi: float
    children: int
    sex: str
    smoker: str
    region: str


@app.post("/predict")
def predict(_: PredictionInput):
    return {"predicted_charges": 1234.56}  # noqa