# # Use the official Python image as the base image
# FROM python:3.9-slim-buster

# # Set the working directory to /app
# WORKDIR /app

# # Copy the requirements file into the container and install the dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # Copy the rest of the application code into the container
# COPY app.py app.py

# # Expose port 5000 for the Flask app
# EXPOSE 5000

# # Start the Flask app when the container starts
# CMD [ "python", "app.py" ]

# Usa un'immagine base leggera di Python
FROM python:3.8-slim

# Imposta il work directory nell'immagine
WORKDIR /app

# Copia i file necessari nel work directory
COPY requirements.txt .
COPY app.py .
# COPY templates/ templates/

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Espone la porta sulla quale l'applicazione Flask ascolterà
EXPOSE 5000

# Comando per eseguire l'applicazione quando il container è in esecuzione
CMD ["python", "app.py"]