from pydantic import BaseModel

# 3. Definizione Modello Pydantic (per validazione dati API)
class Partecipant(BaseModel):
	Name: str
	SurName: str
    WillJoin: bool
	HowManyTotals: int
	HowManyKids: int
	Allergies: str
	AllergiesNotes: str
	Notes: str
