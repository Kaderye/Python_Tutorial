# *args with normal parameter

def multiply_numbers(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_numbers(1,2,3,4,5))

print("_"*50)
# add another parameter like num
# here, first number consider as num numbers 
# so its not multiply
def multiply_numbers(num, *args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_numbers(5,3,4,5))
