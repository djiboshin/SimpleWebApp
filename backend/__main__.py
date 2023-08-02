from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/f")
def read_item():
    return [[1, 1, 1, 1], [1, 2, 3, 4], [4, 4, 4, 4]]
