# Day 13 � Generators & Iterators
# Date: July 06, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

# ============================================
# PYTHON GENERATORS - COMPLETE BEGINNER LESSON
# ============================================

import sys

print("=" * 50)
print("STEP 1: Normal Function (return)")
print("=" * 50)

def normal_function():
    return [1, 2, 3, 4, 5]

lst = normal_function()

print("Returned Value :", lst)
print("Type           :", type(lst))
print("Memory Size    :", sys.getsizeof(lst), "bytes")

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 2: Generator Function (yield)")
print("=" * 50)

def generator_function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = generator_function()

print("Generator Object :", gen)
print("Type             :", type(gen))
print("Memory Size      :", sys.getsizeof(gen), "bytes")

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 3: Getting Values Using next()")
print("=" * 50)

gen = generator_function()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 4: How yield Pauses the Function")
print("=" * 50)

def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3

x = demo()

print(next(x))
print(next(x))
print(next(x))

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 5: Using a for Loop")
print("=" * 50)

def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 6: Memory Comparison")
print("=" * 50)

big_list = list(range(1, 1001))
big_generator = (i for i in range(1, 1001))

print("List Memory      :", sys.getsizeof(big_list), "bytes")
print("Generator Memory :", sys.getsizeof(big_generator), "bytes")

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 7: Your Own Generator")
print("=" * 50)

def create():
    i = 1
    while i <= 5:
        yield i
        i += 1

for value in create():
    print(value)

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 8: Generator Can Be Used Only Once")
print("=" * 50)

g = create()

print("First Time :", list(g))
print("Second Time:", list(g))

# -------------------------------------------------

print("\n" + "=" * 50)
print("STEP 9: List vs Generator")
print("=" * 50)

def list_func():
    return [1, 2, 3]

def gen_func():
    yield 1
    yield 2
    yield 3

print("List Function      :", list_func())
print("Generator Function :", list(gen_func()))

# -------------------------------------------------

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print("""
return:
- Returns all values at once.
- Uses more memory.
- Creates a list.
- Can be reused.

yield:
- Returns one value at a time.
- Uses less memory.
- Creates a generator.
- Can be iterated only once.

Easy Example:
List       -> A bucket full of apples.
Generator  -> An apple tree giving one apple whenever you ask.
""")