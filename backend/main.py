# import contextlib
from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder

app = FastAPI()

# Add a comment to the main endpoint
@app.get("/")
def root():
    return {"message": "API is running"}