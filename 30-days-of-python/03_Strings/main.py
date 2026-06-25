# Day 03 � Strings & Formatting
# Date: June 26, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.
# ======================================================
# DAY 03 - STRINGS & FORMATTING
# ======================================================

import re
import textwrap
from collections import Counter

print("\n" + "=" * 60)
print("DAY 03 - STRINGS & FORMATTING")
print("=" * 60)

# ======================================================
# 1. BASIC STRING OPERATIONS
# ======================================================

print("\n1. BASIC STRING OPERATIONS\n")

name = "Saad"

print("String:", name)
print("Length:", len(name))
print("First Character:", name[0])
print("Last Character:", name[-1])

# Strings are immutable

# name[0] = "A"  # TypeError

new_name = "A" + name[1:]

print("Original:", name)
print("Modified:", new_name)

# ======================================================
# 2. STRING METHODS
# ======================================================

print("\n2. STRING METHODS\n")

text = "   React Node MongoDB Express   "

print("Original:", repr(text))

# strip()

print("\nstrip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

# split()

skills = text.strip().split()

print("\nsplit():", skills)

# join()

joined = " | ".join(skills)

print("join():", joined)

# replace()

sentence = "I love Java"

print("\nreplace():",
      sentence.replace("Java", "Python"))

# find()

message = "Hello Python"

print("\nfind('Python'):", message.find("Python"))
print("find('Java'):", message.find("Java"))

# startswith()

email = "admin@gmail.com"

print("\nstartswith('admin'):",
      email.startswith("admin"))

# endswith()

filename = "profile.jpg"

print("endswith('.jpg'):",
      filename.endswith(".jpg"))

# count()

fruit = "banana"

print("\ncount('a'):", fruit.count("a"))

# isalpha()

print("\n'Python'.isalpha():",
      "Python".isalpha())

print("'Python123'.isalpha():",
      "Python123".isalpha())

# isdigit()

print("\n'12345'.isdigit():",
      "12345".isdigit())

print("'12a45'.isdigit():",
      "12a45".isdigit())


# ======================================================
# 3. STRING SLICING
# ======================================================

print("\n3. STRING SLICING\n")

word = "JavaScript"

print("Word:", word)

print("word[0:4]:", word[0:4])
print("word[:4]:", word[:4])
print("word[4:]:", word[4:])
print("word[::2]:", word[::2])
print("word[-1]:", word[-1])
print("word[-4:]:", word[-4:])
print("Reverse:", word[::-1])

# ======================================================
# 4. STRING FORMATTING
# ======================================================

print("\n4. STRING FORMATTING\n")

name = "Saad"
age = 21
salary = 50000

# f-string

print("F-String:")
print(f"My name is {name} and I am {age} years old.")

# expressions

print(f"10 + 20 = {10 + 20}")

# formatting numbers

print(f"Salary: {salary:,}")

# float precision

pi = 3.14159265359

print(f"Pi: {pi:.2f}")

# debug syntax

print(f"{name=}")
print(f"{age=}")

# .format()

print("\n.format():")

print("My name is {}.".format(name))
print("Name: {}, Age: {}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# old style formatting

print("\n% Formatting:")

print("My name is %s" % name)
print("%s is %d years old" % (name, age))

# ======================================================
# 5. ADVANCED - maketrans()
# ======================================================

print("\n5. str.maketrans()\n")

translation_table = str.maketrans({
    "a": "@",
    "e": "3",
    "i": "1",
    "o": "0"
})

text = "I love Python programming"

translated = text.translate(translation_table)

print("Original:", text)
print("Translated:", translated)

# ======================================================
# 6. TEXTWRAP MODULE
# ======================================================

print("\n6. TEXTWRAP MODULE\n")

paragraph = """
Python is an amazing programming language used in web development,
artificial intelligence, machine learning, automation,
data science and many other domains.
"""

wrapped = textwrap.fill(paragraph, width=40)

print(wrapped)

# ======================================================
# 7. REGEX INTRODUCTION
# ======================================================

print("\n7. REGEX INTRODUCTION\n")

text = """
Contact:
saad@gmail.com
admin@yahoo.com

Order IDs:
12345
67890
"""

# find emails

emails = re.findall(r"\S+@\S+", text)

print("Emails:", emails)

# find numbers

numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)

# match beginning

result = re.match(r"\d+", "123abc")

print("\nStarts with number?:", bool(result))

# search anywhere

search = re.search(r"gmail", text)

print("Contains gmail?:", bool(search))

# replace using regex

sentence = "My phone number is 123456"

new_sentence = re.sub(r"\d+", "XXXXXX", sentence)

print("\nRegex Replace:")
print(new_sentence)

# ======================================================
# EXERCISE 1
# Reverse a string using slicing
# ======================================================

print("\n" + "=" * 60)
print("EXERCISE 1 - REVERSE STRING")
print("=" * 60)

text = "Python"

reverse = text[::-1]

print("Original:", text)
print("Reversed:", reverse)

# ======================================================
# EXERCISE 2
# Parse string to dictionary
# ======================================================

print("\n" + "=" * 60)
print("EXERCISE 2 - PARSE STRING TO DICTIONARY")
print("=" * 60)

data = "name=John;age=30;city=NYC"

result = {}

for item in data.split(";"):
    key, value = item.split("=")
    result[key] = value

print(result)

# ======================================================
# EXERCISE 3
# Palindrome Checker
# ======================================================

print("\n" + "=" * 60)
print("EXERCISE 3 - PALINDROME CHECKER")
print("=" * 60)

text = "A man, a plan, a canal: Panama"

clean = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

print("Cleaned:", clean)

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# ======================================================
# EXERCISE 4
# f-string debug syntax
# ======================================================

print("\n" + "=" * 60)
print("EXERCISE 4 - DEBUG F-STRINGS")
print("=" * 60)

username = "saad_dev"
followers = 1500

print(f"{username=}")
print(f"{followers=}")

# ======================================================
# EXERCISE 5
# Word Frequency Counter
# ======================================================

print("\n" + "=" * 60)
print("EXERCISE 5 - WORD FREQUENCY")
print("=" * 60)

sentence = """
python is easy
python is powerful
python is fun
"""

words = sentence.lower().split()
print(words)

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Using Dictionary:")

for key, value in frequency.items():
    print(f"{key} -> {value}")

print("\nUsing Counter:")

counter = Counter(words)

print(counter)

# ======================================================
# BONUS SECTION
# ======================================================

print("\n" + "=" * 60)
print("BONUS SECTION")
print("=" * 60)

website = "https://github.com"

print("Starts with https:",
      website.startswith("https"))

print("Ends with .com:",
      website.endswith(".com"))

url_parts = website.split("//")

print("Protocol:", url_parts[0][:-1])
print("Domain:", url_parts[1])

# ======================================================
# MINI PROJECT
# USER INFO PARSER
# ======================================================

print("\n" + "=" * 60)
print("MINI PROJECT - USER INFO PARSER")
print("=" * 60)

user_input = "username=saad;role=admin;country=Pakistan"

user = {}

pairs = user_input.split(";")

for pair in pairs:
    key, value = pair.split("=")
    user[key] = value

print(user)

print(f"\nWelcome {user['username']}!")
print(f"Role: {user['role']}")
print(f"Country: {user['country']}")

print("\n" + "=" * 60)
print("DAY 03 COMPLETED SUCCESSFULLY ")
print("=" * 60)