import contextlib
from fastapi import FastAPI, HTTPException, Query
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}