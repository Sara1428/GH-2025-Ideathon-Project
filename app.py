from flask import Flask, request, jsonify
import pytesseract
import cv2
import numpy as np
import sqlite3
import spacy
from werkzeug.utils import secure_filename
import os

# Initializinh Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Loading spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Initializing SQLite database
def init_db():
    os.makedirs("database", exist_ok=True)
    conn = sqlite3.connect("database/pharmacy.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS medicines (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        stock INTEGER)''')
    cursor.executemany("INSERT INTO medicines (name, stock) VALUES (?, ?)", 
                       [("Paracetamol", 50), ("Ibuprofen", 30), ("Amoxicillin", 20)])
    conn.commit()
    conn.close()

init_db()

# OCR Function
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# NLP Processing to extract medicines
def extract_medicines(text):
    doc = nlp(text)
    medicines = []
    for ent in doc.ents:
        if ent.label_ in ["DRUG", "PRODUCT"]:
            medicines.append(ent.text)
    return list(set(medicines))  # Remove duplicates

# Matching medicines with database
def match_with_inventory(medicines):
    conn = sqlite3.connect("database/pharmacy.db")
    cursor = conn.cursor()
    order_list = []
    for medicine in medicines:
        cursor.execute("SELECT name, stock FROM medicines WHERE name LIKE ?", (f"%{medicine}%",))
        result = cursor.fetchone()
        if result:
            order_list.append({"medicine": result[0], "available_stock": result[1]})
    conn.close()
    return order_list

# API Endpoint to process prescription
@app.route('/process-prescription', methods=['POST'])
def process_prescription():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    text = extract_text(file_path)
    medicines = extract_medicines(text)
    order = match_with_inventory(medicines)
    
    return jsonify({"extracted_medicines": medicines, "order": order})

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "running"}), 200

# Running the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
