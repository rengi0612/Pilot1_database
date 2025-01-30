from pymongo import MongoClient
import base64
import logging
import gridfs
from PIL import Image
import io

#logging.basicConfig(level=logging.DEBUG)

class MongoSingleton():

    _instances = {}

    def __call__(self, *args, **kwds):
        if self not in self.instances:
            self._instances[self] = super().__call__(*args, **kwds)
        return self._instances[self]

class MongoDatabase(MongoSingleton):

    _UPLOAD_DIR = "uploads"

    _DOWNLOAD_DIR = "downloads"

    def __init__(self):
        self.client = ""
        self.db = ""
        self.collection = ""
        self.fs = ""


    def auth(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client["piloto1_database"]   
            self.collection = self.db["images"]
            self.fs = gridfs.GridFS(self.db)
            print("Authentication successful! MongoDB connection is working.")
        except Exception as e:
            print(f"Authentication failed: {e}")

    # Save an image as Base64
    def saveImage(self, file: str):
        try:
            file_location = f"{self._UPLOAD_DIR}/{file}"
            image_data = ""
            with open(file_location, "rb") as file_read:
                image_data = file_read.read()
            print(type(image_data))
            file_id = self.fs.put(image_data, filename=file, format="jpg")
            print(f"Image saved to GridFS with file ID: {file_id}")
        except Exception as e:
            print(e)
        print("Image uploaded!")

    # Retrieve image
    def retrieveImage(self, file: str):
        file_metadata = self.fs.find_one({"filename": file})
        file_location = f"{self._DOWNLOAD_DIR}/{file}"
        if file_metadata:
            # Convert binary data back to an image
            image = Image.open(io.BytesIO(file_metadata.read()))
            #image.show()  # Display the image
            image.save(file_location)  # Save the image to a file
            print(f"Image retrieved and saved as {file}")
        else:
            print("Image not found in GridFS.")
        print("Image downloaded!")





