from fastapi import FastAPI, HTTPException
from .database import engine, SessionLocal
import json
from . import models
from .models import PartecipantDB
from .partecipant import Partecipant


# Inizializza tutte le tabelle definite in models.py
models.Base.metadata.create_all(bind=engine)

# 4. Inizializzazione App
app = FastAPI()

# 5. Endpoint API
@app.get("/")
def read_root():
    return {"message": "API Matrimonio Funzionanti!"}

@app.post("/partecipants/")
def create_partecipant(partecipant: Partecipant):
    db = SessionLocal()

    # 1. Cerca un partecipante esistente per Name e SurName
    db_partecipant = db.query(PartecipantDB).filter(
        PartecipantDB.Name == partecipant.Name,
        PartecipantDB.SurName == partecipant.SurName
    ).first()

    if db_partecipant:
        # 2. Se il record ESISTE, AGGIORNA i campi
        
        # Aggiorna solo i campi che non sono Name, SurName o id
        db_partecipant.WillJoin = partecipant.WillJoin
        db_partecipant.HowManyTotals = partecipant.HowManyTotals
        db_partecipant.HowManyKids = partecipant.HowManyKids
        db_partecipant.Allergies = partecipant.Allergies
        db_partecipant.AllergiesNotes = partecipant.AllergiesNotes
        db_partecipant.Notes = partecipant.Notes
        # L'oggetto è già "dirty" (modificato) in SQLAlchemy. Non serve db.add().
        
    else:
        # 3. Se il record NON ESISTE, CREA un nuovo record
        db_partecipant = PartecipantDB(
            Name = partecipant.Name,
            SurName = partecipant.SurName,
            WillJoin = partecipant.WillJoin,
            HowManyTotals = partecipant.HowManyTotals,
            HowManyKids = partecipant.HowManyKids,
            Allergies = partecipant.Allergies,
            AllergiesNotes = partecipant.AllergiesNotes,
            Notes = partecipant.Notes,
        )
        db.add(db_partecipant)

    # 4. Esegui il commit delle modifiche (inserimento o aggiornamento)
    try:
        db.commit()
        db.refresh(db_partecipant)
    except Exception as e:
        db.rollback()
        db.close()
        raise HTTPException(status_code=500, detail=f"Errore DB durante l'upsert: {e}")
        
    db.close()
    return db_partecipant


@app.get("/partecipants/")
def read_guests():
    db = SessionLocal()
    guests = db.query(PartecipantDB).all()
    db.close()
    return guests