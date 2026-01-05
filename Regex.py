import re
import json

# ---------------- Q1 ----------------
# Take document text and convert to lowercase
text = input("Enter document text: ")
text_lower = text.lower()
print("\nQ1 - Lowercase Text:")
print(text_lower)

# ---------------- Q2 ----------------
# Remove noise such as !!!, /-, commas, and emojis
# Remove punctuation
clean_text = re.sub(r"[!,/\\\-]", "", text_lower)

# Remove emojis (basic unicode range)
clean_text = re.sub(r"[^\w\s:/]", "", clean_text)

print("\nQ2 - Cleaned Text:")
print(clean_text)

# ---------------- Q3 ----------------
# Extract amount value using string operations
amount_value = None
words = clean_text.split()
for word in words:
    if word.isdigit():
        amount_value = int(word)
        break

print("\nQ3 - Extracted Amount (String Ops):")
print(amount_value)

# ---------------- Q4 ----------------
# Extract all numbers using regex
numbers = re.findall(r"\d+", clean_text)
print("\nQ4 - All Numbers Found:")
print(numbers)

# ---------------- Q5 ----------------
# Extract date in DD/MM/YYYY format
date_match = re.search(r"\b\d{2}/\d{2}/\d{4}\b", clean_text)
date_value = date_match.group() if date_match else None

print("\nQ5 - Extracted Date:")
print(date_value)

# ---------------- Q6 ----------------
# Combine preprocessing + regex to extract date and amount
amount_regex = re.search(r"\b\d{4,}\b", clean_text)
amount_final = int(amount_regex.group()) if amount_regex else None

print("\nQ6 - Date and Amount:")
print("Date:", date_value)
print("Amount:", amount_final)

# ---------------- Q7 ----------------
# Create JSON object
document_data = {
    "date": date_value,
    "amount": amount_final
}

print("\nQ7 - JSON Object:")
print(document_data)

# ---------------- Q8 ----------------
# Save JSON to file
with open("document_data.json", "w") as file:
    json.dump(document_data, file, indent=4)

print("\nQ8 - JSON saved to document_data.json")

# ---------------- Q9 ----------------
# Read JSON file and print values
with open("document_data.json", "r") as file:
    loaded_data = json.load(file)

print("\nQ9 - Read JSON Data:")
print(loaded_data)

# ---------------- Q10 ----------------
# Update status based on amount
if loaded_data["amount"] is not None and loaded_data["amount"] > 40000:
    loaded_data["status"] = "HIGH VALUE"
else:
    loaded_data["status"] = "NORMAL"

# Save updated JSON
with open("document_data.json", "w") as file:
    json.dump(loaded_data, file, indent=4)

print("\nQ10 - Updated JSON with Status:")
print(loaded_data)
