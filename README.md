# AI-Powered Pharmacist Assistant

## 📌 Project Overview
This **AI-Powered Pharmacist Assistant** is a Flask-based AI solution that automates the processing of handwritten prescriptions using **Optical Character Recognition (OCR)** and **Natural Language Processing (NLP)**. It extracts medicine names from prescription images, matches them with a pharmacy inventory, and generates structured orders.

---

## 🚀 Features
- ✅ **OCR Processing**: Extracts text from handwritten prescriptions using **Tesseract OCR**.
- ✅ **NLP Entity Recognition**: Uses **spaCy** to identify medicine names and dosages.
- ✅ **Database Matching**: Matches extracted medicines with a pharmacy’s inventory stored in **SQLite**.
- ✅ **Automated Order Generation**: Creates a structured order for pharmacists to review and dispense.
- ✅ **API-Driven**: Flask-based REST API for easy integration with other systems.

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **AI/ML:** Tesseract OCR, spaCy NLP
- **Database:** SQLite
- **Deployment:** Docker, Google Cloud Run

---

## Project Structure
 📂 [database](https://github.com/Sara1428/GH-2025-Ideathon-Project/tree/main/database)  <br>
  &nbsp; &nbsp; &nbsp; &nbsp;     ├── [pharmacy.db](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/database/pharmacy.db)    --> SQLite database    <br>
  &nbsp; &nbsp; &nbsp; &nbsp;  ├── [init_db.py](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/database/init_db.py)        --> Database initialization script <br>

 📂 [models](https://github.com/Sara1428/GH-2025-Ideathon-Project/tree/main/models)  <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── [ocr.py](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/models/ocr.py)           --> OCR extraction logic   <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── [nlp.py](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/models/nlp.py)            --> NLP processing for medicine detection    <br>

📂 [uploads](https://github.com/Sara1428/GH-2025-Ideathon-Project/tree/main/uploads)      --> Directory for prescription image uploads  <br>   

📂 [tests](https://github.com/Sara1428/GH-2025-Ideathon-Project/tree/main/tests)  <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── [test_api.py](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/tests/test_api.py)       --> Unit tests for API  <br> 
&nbsp; &nbsp; &nbsp; &nbsp;  <br>
[app.py](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/app.py)                   --> Main Flask API application   <br>

[requirements.txt](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/requirements.txt)       --> Python dependencies  <br>

[Dockerfile](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/Dockerfile)               --> Containerization setup <br>

[docker-compose.yml](https://github.com/Sara1428/GH-2025-Ideathon-Project/blob/main/docker-compose.yml)       -->  Multi-container deployment<br>

