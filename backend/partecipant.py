from pydantic import BaseModel
from datetime import datetime

# Definizione Modello Pydantic (per validazione dati API)
class Partecipant(BaseModel):
	Name: str
	SurName: str
	WillJoin: bool
	HowManyTotals: int
	HowManyKids: int
	Allergies: str
	AllergiesNotes: str
	Notes: str
	updated_at: datetime | None = None
