"""
Problem: Write a program to Find the Largest Number Among Three Numbers
"""

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

def greatest_number(number_1,number_2,number_3):
    if number_1>number_2 and number_1>number_3:
        print(f"{number_1} is greater than {number_2} and {number_3}")
    elif number_2>number_1 and number_2>number_3:
        print(f"{number_2} is greater than {number_1} and {number_3}")
    else:
        print(f"{number_3} is greater than {number_1} and {number_2}")

greatest_number(number_1,number_2,number_3)