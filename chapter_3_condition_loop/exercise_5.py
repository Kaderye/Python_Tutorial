"""
Problem 1: Ask user to input a number containing more than one digit
Example: 24589
Calculate 2*4*5*8*9 and print
"""

number = input("Enter a number: ")

i = 0
mul = 1
while(i < len(number)):
    mul = mul * int(number[i])
    i += 1

print(f"The result of {number} is {mul}")
