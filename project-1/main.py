from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Project 1 (minimal)!"}


# Exemple d'endpoint supplémentaire
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is a sample item."}
