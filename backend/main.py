from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import PartecipantDB

# # 1. Configurazione Database SQLite
# DATABASE_URL = "sqlite:///./wedding_data/wedding.db" # Nota il percorso cartella
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Crea le tabelle all'avvio
# Base.metadata.create_all(bind=engine)

# 4. Inizializzazione App
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Matrimonio Funzionanti!"}