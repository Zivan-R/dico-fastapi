from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import httpx

from .models import DictionaryRequest
from .database import sessionLocal, base, engine

base.metadata.create_all(bind=engine)

class WordQuery(BaseModel):
    word: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/lookup")
async def lookup_word(query: WordQuery):
    word = query.word.lower()
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    
    if resp.status_code != 200:
        raise HTTPException(status_code=404, detail="Word not found")
    
    data = resp.json()
    
    try:
        db = sessionLocal()
        entry = DictionaryRequest(word=word, response_json=data)
        db.add(entry)
        db.commit()
    except Exception as e:
        print(f"Failed to store in db: {e}")
    finally:
        db.close()
    
    return data

