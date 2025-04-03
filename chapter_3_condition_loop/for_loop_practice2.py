"""
Problem 1: Ask user to input a number containing more than one digit
Example: 24589
Calculate 2*4*5*8*9 and print
"""

number = input("Enter a number: ")

mul = 1
for i in range(len(number)):
    mul = mul * int(number[i])
    i += 1

print(f"The result of {number} is {mul}")
