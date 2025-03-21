from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from Project 2 (minimal)!"}


@app.get("/predict")
def predict():
    # Exemple d'une prédiction fictive
    return {"prediction": 123.45}