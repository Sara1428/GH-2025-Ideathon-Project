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
 📂 database  <br>
  &nbsp; &nbsp; &nbsp; &nbsp;     ├── pharmacy.db    --> SQLite database    <br>
  &nbsp; &nbsp; &nbsp; &nbsp;  ├── init_db.py        --> Database initialization script <br>

 📂 models  <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── ocr.py           --> OCR extraction logic   <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── nlp.py            --> NLP processing for medicine detection    <br>

 📂 static  <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── 📂 uploads       --> Directory for prescription image uploads  <br>   
📂 tests  <br>
&nbsp; &nbsp; &nbsp; &nbsp;   ├── test_api.py       --> Unit tests for API  <br> 
&nbsp; &nbsp; &nbsp; &nbsp;  <br>
app.py                   --> Main Flask API application   <br>

requirements.txt       --> Python dependencies  <br>

Dockerfile               --> Containerization setup <br>

docker-compose.yml       -->  Multi-container deployment<br>

