from fastapi import FastAPI, HTTPException
from .database import engine, SessionLocal
import json
from . import models, partecipant



# Inizializza tutte le tabelle definite in models.py
models.Base.metadata.create_all(bind=engine)

# 4. Inizializzazione App
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Matrimonio Funzionanti!"}