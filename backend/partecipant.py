from pydantic import BaseModel
from datetime import datetime
import typing # Importiamo l'intero modulo per evitare NameError

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
	updated_at: typing.Union[datetime, None] = None
