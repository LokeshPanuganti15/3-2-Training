import json
student_data = {
    "name": "Lokesh Panuganti",
    "roll_number": 373,
    "marks": 100
}
with open("student.json", "w") as f:
    json.dump(student_data, f, indent=4)
with open("student.json", "r") as f:
    data = json.load(f)
print("Full JSON Data:", data)
print(f"Name: {data['name']}")
print(f"Roll Number: {data['roll_number']}")
print(f"Marks: {data['marks']}")
result = "Pass" if data["marks"] >= 40 else "Fail"
print(f"Result: {result}")
data["result"] = result
with open("student_result.json", "w") as f:
    json.dump(data, f, indent=4)

print("Updated JSON saved to student_result.json")