
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base # Importa la Base dal file appena creato

# Definizione Modello DB (Tabella Ospiti)
class PartecipantDB(Base):
    __tablename__ = "Partecipants"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    SurName = Column(String, index=True)
    WillJoin = Column(Boolean, default=False)
    HowManyTotals = Column(Integer, default=0)
    HowManyKids = Column(Integer, default=0)
    Allergies = Column(String, default='')
    AllergiesNotes = Column(String, default='')
    Notes = Column(String, default='')

