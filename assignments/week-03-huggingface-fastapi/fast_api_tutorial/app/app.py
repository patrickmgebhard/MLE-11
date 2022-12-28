from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

pipeline = pipeline(model="model/t5_small", task="translation_en_to_de")

app = FastAPI()

class TextToTranslate(BaseModel):
    input_text: str

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)