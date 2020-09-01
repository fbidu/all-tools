"""
Dummy API to be used with tools that work on REST APIs

"but this code makes no sense" - yes, I know
"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """
    Welcome!
    """
    return "Hello!"


@app.get("/translate/{name}", response_model=str)
def name_translator(name: str):
    """
    A broken string decoder-encoder. Will fail on any input with
    a non-ASCII character such as "joão".
    """
    return name.encode("UTF-8").decode("ascii")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
