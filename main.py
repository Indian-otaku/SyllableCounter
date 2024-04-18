from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from syllable_counter import find_syllable_count_from_sentences

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/api/syllable_count")
async def get_syllable_count(text_data: TextData):
    text = text_data.text
    syllable_count = find_syllable_count_from_sentences(text)
    return {
        "syllable_count": syllable_count
    }
    

if __name__ == '__main__':
	uvicorn.run(app, port=8000, host="127.0.0.1")