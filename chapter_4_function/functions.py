# functions
# name = "kaderye"
# print(len(name))

# sum the two numbers using a function
number_1 = int(input("Enter the value of number_1: "))
number_2 = int(input("Enter the value of number_2: "))

def add_two(number_1,number_2):
    return number_1+number_2

print(f"The summation of {number_1} and {number_2} is {add_two(number_1,number_2)}")



# add two strings 
first_name = input("Enter the first name: ")
last_name = input("Enter the second name: ")

def add_string(a,b):
    return a+ b

print(f"Full name is {add_string(first_name,last_name)}")