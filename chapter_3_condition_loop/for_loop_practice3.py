"""
Problem 1: Ask user to input a number containing more than one digit
Example: 24589
Calculate 2^2+4^2+5^2+8^2+9^2 and print
"""

number = input("Enter a number: ")

sum = 0
for i in range(len(number)):
    sum = sum + (int(number[i])**2)
    i += 1

print(f"The summation of {number} is {sum}")
