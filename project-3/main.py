from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Project 3 - Template"} # noqa