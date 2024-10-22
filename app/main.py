from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_hello():
    return {"message": "Hello, World!"}

@app.get("/greet")
def greet_name(name: str):
    return {"message": f"{name}, hello"}
