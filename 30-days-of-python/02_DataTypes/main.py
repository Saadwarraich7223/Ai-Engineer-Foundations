# ==========================================
# DAY 02 - DATA TYPES & TYPE CONVERSION
# ==========================================

print("\n========== 1. BUILT-IN DATA TYPES ==========\n")

# Immutable Types

integer_num = 10
float_num = 10.5
is_logged_in = True
name = "Saad"
coordinates = (10, 20)
unique_nums = frozenset([1, 2, 3])
binary_data = b"Hello"

print(integer_num, type(integer_num))
print(float_num, type(float_num))
print(is_logged_in, type(is_logged_in))
print(name, type(name))
print(coordinates, type(coordinates))
print(unique_nums, type(unique_nums))
print(binary_data, type(binary_data))


# Mutable Types

numbers = [1, 2, 3]
user = {"name": "Saad", "age": 21}
my_set = {1, 2, 3}
mutable_bytes = bytearray(b"Hello")

print("\nMutable Types:")
print(numbers, type(numbers))
print(user, type(user))
print(my_set, type(my_set))
print(mutable_bytes, type(mutable_bytes))


# ==========================================
print("\n========== 2. MUTABILITY DEMO ==========\n")

# List is mutable

numbers.append(4)
print("List after append:", numbers)

# Dictionary is mutable

user["city"] = "Lahore"
user['country']='Pakistan'
print("Updated Dictionary:", user)

# Set is mutable

my_set.add(4)
print("Updated Set:", my_set)

# Strings are immutable

text = "Python"

# text[0] = "J" # Uncomment to see error

new_text = "J" + text[1:]
print("Original String:", text)
print("Modified String:", new_text)


# ==========================================
print("\n========== 3. TYPE CONVERSION ==========\n")

# int()

age = int("21")
print(age, type(age))

# float()

price = float("19.99")
print(price, type(price))

# str()

num = 100
num_str = str(num)
print(num_str, type(num_str))

# list()

letters = list("Python")
print(letters)

# tuple()

my_tuple = tuple([1, 2, 3])
print(my_tuple)

# set()

unique = set([1, 1, 2, 2, 3])
print(unique)

# dict()

person = dict(name="Saad", age=21)
print(person)

# bool()

print(bool(1))
print(bool(0))


# ==========================================
print("\n========== 4. SAFE TYPE CONVERSION ==========\n")

strings = ["10", "20", "abc", "40", "50xyz"]

integers = []

for item in strings:
    try:
        integers.append(int(item))
    except ValueError:
        print(f"Cannot convert '{item}' to integer")

print("Converted Integers:", integers)


# ==========================================
print("\n========== 5. FALSY VALUES ==========\n")

falsy_values = [
    False,
    None,
    0,
    0.0,
    "",
    [],
    (),
    {},
    set(),
    frozenset(),
    range(0)
]

for value in falsy_values:
    print(f"{repr(value):15} -> {bool(value)}")


# ==========================================
print("\n========== 6. TRUTHY VALUES ==========\n")

truthy_values = [
    True,
    1,
    -1,
    3.14,
    "Hello",
    [1],
    (1,),
    {"name": "Saad"},
    {1, 2},
]

for value in truthy_values:
    print(f"{repr(value):20} -> {bool(value)}")


# ==========================================
print("\n========== 7. NONE TYPE ==========\n")

x = None

print("Value:", x)
print("Type:", type(x))

if x is None:
    print("x contains no value")


# ==========================================
print("\n========== 8. type() VS isinstance() ==========\n")

num = 10

print(type(num))
print(type(num) == int)

print(isinstance(num, int))
print(isinstance(num, (int, float)))


# ==========================================
print("\n========== 9. CHECK TYPES OF LITERALS ==========\n")

values = [
    1,
    1.0,
    True,
    "Hello",
    [1, 2],
    (1, 2),
    {1, 2},
    {"name": "Saad"},
    None,
    b"hello"
]

for value in values:
    print(f"{repr(value):25} -> {type(value)}")


# ==========================================
print("\n========== 10. FLOAT PRECISION PROBLEM ==========\n")

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 :", (0.1 + 0.2) == 0.3)


# ==========================================
print("\n========== 11. SOLVING FLOAT PRECISION ==========\n")

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print("Decimal Result:", a + b)
print("Decimal Comparison:", (a + b) == Decimal("0.3"))


# ==========================================
print("\n========== 12. IDENTITY VS EQUALITY ==========\n")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b :", a == b)  # value comparison
print("a is b :", a is b)  # object comparison

print("a == c :", a == c)
print("a is c :", a is c)


# ==========================================
print("\n========== 13. BONUS: MEMORY ADDRESS ==========\n")

x = 100
y = x

print("id(x):", id(x))
print("id(y):", id(y))


# ==========================================
print("\n========== DAY 02 COMPLETED ==========\n")