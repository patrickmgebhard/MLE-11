from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# this is the code snippet from the t5-small page
"""from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-small")

model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
"""
#pipeline = pipeline("")
#en_fr_translator = pipeline("translation_en_to_fr")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)