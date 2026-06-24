# Day 01 � Variables & Scope
# Date: June 24, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.

# Scope Global
me='Saad'
age=24
education='Computer Science'

# print(name)
# print(age)
# print(education)



# print(name+" is "+str(age)+" of years age ."+name+" studies in "+education) #concatination
# print(f"{name} is {age} years old and studies in {education}") # using f string (much cleaner)


# Scope : local
def name():
    language="python"

    print(me) #Globally declared variables can be used anywhere
    print(language)

name()
# print(language)  #Local variables cannot be used outside of its scope



#  Coding Practice Questions
# Q1: Write a program that stores your name, age, and country and prints them using an f-string.
# Q2: Write a program that stores your favorite subject, marks, and grade, then prints a sentence using an f-string.
# Q3: Write a program that stores your city, temperature, and weather condition, then displays them in one sentence.
# Q4: Write a program that stores your first name and last name, then prints your full name using an f-string.
# Q5: Write a program that stores your product name, price, and quantity, then prints a bill summary using an f-string.


#====================== SOLUTIONS ===================================

#Q1
my_name="Muhammad Saad"
my_age=24
my_country="Pakistan"

print(f"My name is {my_name}. I am {my_age} years old and i live in {my_country}.")

#Q2
fav_subject="Deep Learning"
marks=60
grade="Average"

print(f"My favorite subject is {fav_subject}. Even though {fav_subject} is my favorite subject i would be able to secure about {marks}% marks with an {grade} passing grade.")

#I Understood the topic well enough and do not need to waste my time any longer on further questions-If you want to practice more , solve all these questions. 


#Day_1 Completed 