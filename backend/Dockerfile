# Usa un'immagine Python leggera
FROM python:3.9-slim

# Imposta la cartella di lavoro nel container
WORKDIR /app

# Copia i requirements e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice
COPY . /app/backend

# Crea la cartella per il DB dentro il container
RUN mkdir -p /app/backend/wedding_data

# Comando di avvio
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]