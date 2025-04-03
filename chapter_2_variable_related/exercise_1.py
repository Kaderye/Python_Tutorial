"""
Exercise 1: Ask user to input 3 numbers and you have to print average of three numbers using string formatting
Hints: try to take all three comma separated inputs in one line
"""

number_1, number_2, number_3 = input("Enter the three numbers separated by comma: ").split(",")
sum = int(number_1)+int(number_2)+int(number_3)
average = sum/3
print(f"The average of {number_1}, {number_2} and {number_3} is {average}")

print(f"The average is {(int(number_1)+int(number_2)+int(number_3))/3}")