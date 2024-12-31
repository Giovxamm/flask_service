# Usa un'immagine leggera di Python
FROM python:3.9-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file delle dipendenze
COPY requirements.txt requirements.txt

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il codice sorgente
COPY . .

# Espone la porta
EXPOSE 5000

# Avvia l'applicazione
CMD ["python", "app.py"]