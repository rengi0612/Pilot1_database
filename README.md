# Pilot1_database

## This repo contains all the logic for Piloto1 database API and database

## Installation
1. Fork the repository

2. CLone the repository

3. Create a virtual env to manage specific dependencies
    ```bash
   virtualenv <name>
   ```
4. Activate virtualenv
    ```bash
   .\<name>\Scripts\activate
   ```
5. Install dependencies
    ```bash
   pip install -r requirements.txt
   ```
6. Install docker desktop
    https://www.docker.com/products/docker-desktop/
7. (Optional) Install mongodb 
    https://www.mongodb.com/products/tools/compass
8. Install some API software like Postman, Insomnia, python requests etc.

## Usage
1. In root start docker
    ```bash
   docker-compose up -d
   ```
2. In another bash/powershell window, start uvicorn service
    ```bash
   uvicorn main:app --reload
   ```
3. Using API software hit the endpoints
* Save Image
    ```bash
   curl -X 'POST' \
  'http://127.0.0.1:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@imagen.jpg'
  ```

* Get Image
    ```bash
   curl -X GET "http://127.0.0.1:8000/images/imagen.jpg" --output imagen_descargada.jpg
   ```