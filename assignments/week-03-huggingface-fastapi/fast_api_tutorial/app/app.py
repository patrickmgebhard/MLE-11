from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from typing import List

pipeline = pipeline(model="model/t5_small", task="translation_en_to_de")

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

# need to fix this!
class TextsToTranslate(BaseModel):
    input_texts: List[str]

@app.get("/")
def index():
    return {"message": "Hello World"}
    
@app.get("/ping")
def ping():
    return {"message": "ping"}

@app.post("/echo")
def echo(text_to_translate: TextToTranslate):
    return {"message": text_to_translate.input_text}

@app.post("/translate")
def translate(text):
    return pipeline(text)

@app.post("/translating")
def translating(texts_to_translate: TextsToTranslate):
    return pipeline(texts_to_translate.input_texts)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)