from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os
from db_central import MongoDatabase as db

app = FastAPI()

UPLOAD_DIR = "uploads"
DOWNLOAD_DIR = "downloads" 
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Crea la carpeta si no existe
os.makedirs(DOWNLOAD_DIR, exist_ok=True)  # Crea la carpeta si no existe

database = db()
database.auth()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    
    # Guardar la imagen en el servidor
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    database.saveImage(file.filename)
    return {"filename": file.filename, "message": "Imagen subida exitosamente"}

@app.get("/images/{filename}")
async def get_image(filename: str):
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    database.retrieveImage(file = filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "Imagen no encontrada"}

# Endpoint de prueba
@app.get("/")
def home():
    return {"message": "API de subida de imágenes funcionando"}