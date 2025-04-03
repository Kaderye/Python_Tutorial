"""
Problem 1: Ask user to input a number containing more than one digit
Example: 24589
Calculate 2+4+5+8+9 and print
"""

number = input("Enter a number: ")

i = 0
sum = 0
while(i < len(number)):
    sum = sum + int(number[i])
    i += 1

print(f"The summation of {number} is {sum}")
