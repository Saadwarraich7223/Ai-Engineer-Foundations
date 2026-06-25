# Day 04 � Lists & List Operations
# Date: June 27, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.


# List is like an array but more flexible (Mutable)
from collections import deque
import copy

print("=== LIST METHODS ===")

nums = [10, 20, 30]

# append
nums.append(40)

# extend
nums.extend([50, 60])

# insert
nums.insert(1, 15)

# remove
nums.remove(30)

# pop
last = nums.pop()

# index
print("Index of 20:", nums.index(20))

# count
nums.append(20)
print("Count of 20:", nums.count(20))

# sort
nums.sort()

# reverse
nums.reverse()

# copy
new_nums = nums.copy()

print(nums)
print(new_nums)

# -----------------------------------------

print("\n=== SLICING ===")

numbers = [1, 2, 3, 4, 5, 6]

numbers = [10, 20, 30, 40, 50]

# Get elements from index 1 up to (but not including) index 4
# Indexes selected: 1, 2, 3
# Result: [20, 30, 40]
print(numbers[1:4])

# Reverse the entire list using a step of -1
# Result: [50, 40, 30, 20, 10]
print(numbers[::-1])

# Get every second element starting from index 0
# Indexes selected: 0, 2, 4
# Result: [10, 30, 50]
print(numbers[::2])

# Get elements from the beginning up to (but not including) index 2
# Indexes selected: 0, 1
# Result: [10, 20]
print(numbers[:2])

# Shallow Copy

a = [1, 2, [3, 4]]
b = a.copy()

b[2][0] = 100

print("Original:", a)
print("Shallow:", b)

# Deep Copy

c = copy.deepcopy(a)
c[2][0] = 999

print("Deep Copy:", c)
print("Original:", a)

# -----------------------------------------

print("\n=== ENUMERATE ===")

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# -----------------------------------------

print("\n=== ZIP ===")

names = ["Ali", "Saad", "Ahmed"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)

# -----------------------------------------

print("\n=== MAP ===")

nums = [1, 2, 3, 4]

squares = list(map(lambda x: x ** 2, nums))

print(squares)

# -----------------------------------------

print("\n=== FILTER ===")

nums = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)

# -----------------------------------------

print("\n=== SORTED ===")

nums = [5, 2, 8, 1]

print(sorted(nums))
print(nums)

# -----------------------------------------

print("\n=== REVERSED ===")

nums = [1, 2, 3, 4]

print(list(reversed(nums)))

# -----------------------------------------

print("\n=== STACK ===")

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print(stack.pop())
print(stack)

# -----------------------------------------

print("\n=== QUEUE ===")

queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())
print(queue)

# -----------------------------------------

print("\n=== NESTED LIST ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])

# -----------------------------------------

print("\n=== MATRIX TRANSPOSE ===")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = []

for col in range(len(matrix[0])):
    row = []

    for r in matrix:
        row.append(r[col])

    transpose.append(row)

print(transpose)

# Using zip

transpose2 = list(zip(*matrix))

print(transpose2)