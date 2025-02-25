import spacy

nlp = spacy.load("en_core_web_sm")

def extract_medicines(text):
    doc = nlp(text)
    medicines = []
    for ent in doc.ents:
        if ent.label_ in ["DRUG", "PRODUCT"]:
            medicines.append(ent.text)
    return list(set(medicines))  # Removing duplicates
