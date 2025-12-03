from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./wedding_data/wedding.db" 

# Connessione al DB
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} # Necessario per SQLite con FastAPI
)

# Funzione per creare una sessione DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# La classe Base che tutti i modelli devono ereditare
Base = declarative_base()