import json

# Path to your .jsonl file
input_file = r'C:\Users\smallam1\Documents\Homework 1\Model data\training_newdata.jsonl'
# Path to the output .json file
output_file = r'C:\Users\smallam1\Documents\Homework 1\Model data\training_newdata.json'

# Read the .jsonl file and convert it to a list of dictionaries
data = []
try:
    with open(input_file, 'r', encoding='utf-8') as f:  # Try reading with UTF-8 encoding first
        for line in f:
            data.append(json.loads(line))
except UnicodeDecodeError:
    with open(input_file, 'r', encoding='utf-16') as f:  # Fallback to UTF-16 if UTF-8 fails
        for line in f:
            data.append(json.loads(line))

# Write the list of dictionaries to a .json file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
