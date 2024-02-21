import spacy
from spacy.tokens import DocBin
import json

# Load your spaCy model
nlp = spacy.blank("en")  # Use the correct model for your language

# Load your JSON data
with open(r"c:\Users\smallam1\Documents\Homework 1\Model data\training_newdata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Assuming the data might be a list of records like the one provided
# If it's just a single record, wrap it in a list: data = [data]

doc_bin = DocBin()  # Create a DocBin object for saving Docs

for record in data:
    text = record["text"]
    doc = nlp.make_doc(text)  # Create a Doc from the text

    ents = []
    for span in record.get("spans", []):  # Handle cases where "spans" might be missing or empty
        start = span["start"]
        end = span["end"]
        label = span["label"]
        span = doc.char_span(start, end, label=label)
        if span is not None:  # Ensure the span is valid
            ents.append(span)
    doc.ents = ents  # Set the document's entities
    
    doc_bin.add(doc)  # Add the doc to the DocBin

# Save the DocBin to a file
doc_bin.to_disk(r"c:\Users\smallam1\Documents\Homework 1\Model data\training_newdata.spacy")
