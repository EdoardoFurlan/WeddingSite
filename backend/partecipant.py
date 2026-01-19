from pydantic import BaseModel

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
    updated_at: Optional[datetime] = None