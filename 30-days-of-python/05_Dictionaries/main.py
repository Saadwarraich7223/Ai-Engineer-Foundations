# Day 05 � Dictionaries & Sets
# Date: June 28, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

student = {
    "name": "Saad",
    "age": 20,
    "city": "Lahore"
}

print(student["name"])      # Saad
print(student.get("age"))   # 20

student["age"] = 21
student["email"] = "saad@example.com"

for key, value in student.items():
    print(key, ":", value)



numbers = {1, 2, 3, 3, 4, 4, 5}

print(numbers)  # Duplicates removed

numbers.add(6)
numbers.remove(2)

for num in numbers:
    print(num)
    
    
    
contacts = {
    "Saad": "12345",
    "Ali": "67890",
    "Saad": "12345"
}

unique_numbers = set(contacts.values())

print("Contacts:", contacts)
print("Unique Numbers:", unique_numbers)