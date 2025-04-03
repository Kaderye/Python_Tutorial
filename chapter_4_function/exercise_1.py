"""
Problem: Define a function which takes two numbers 
as an input and return greater, equal or less of two numbers
"""

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

def greater_number(number_1, number_2):
    if number_1>number_2:
        print(f"{number_1} is greather than {number_2}")
    elif number_1 == number_2:
        print(f"{number_1} is equal to {number_2}")
    else:
        print(f"{number_1} is less than {number_2}")

greater_number(number_1, number_2)