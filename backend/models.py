from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from .database import Base

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
    # Usa questa versione per debuggare:
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)