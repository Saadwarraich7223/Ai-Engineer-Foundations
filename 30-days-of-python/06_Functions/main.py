# Day 06 � Functions & Lambdas
# Date: June 29, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

# =========================
# FUNCTIONS (USEFUL BASICS)
# =========================

# 1. Simple function
def greet(name):
    return f"Hello, {name}"

print(greet("Saad"))


# 2. Default parameter
def greet_user(name="Guest"):
    return f"Hello, {name}"

print(greet_user())
print(greet_user("Ali"))


# 3. Multiple parameters
def add(a, b):
    return a + b

print(add(5, 3))


# 4. *args (multiple values)
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4, 5))


# 5. **kwargs (named values)
def show_user(**info):
    for key, value in info.items():
        print(key, ":", value)

show_user(name="Saad", age=20, city="Lahore")


# =========================
# LAMBDAS (SHORT FUNCTIONS)
# =========================

# 6. Simple lambda
square = lambda x: x * x
print(square(5))


# 7. Lambda with map (transform data)
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)


# 8. Lambda with filter (select data)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 9. Lambda with sort (very useful in real projects)
students = [
    {"name": "Ali", "marks": 70},
    {"name": "Saad", "marks": 90},
    {"name": "Ahmed", "marks": 80}
]

students.sort(key=lambda s: s["marks"])
print(students)


# =========================
# SIMPLE REAL EXAMPLE
# =========================

def get_top_student(students):
    return max(students, key=lambda s: s["marks"])

print("Top Student:", get_top_student(students))