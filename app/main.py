from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ma_fonction():
    return {"message": "hello"}