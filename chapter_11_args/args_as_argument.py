# args as argument

num = int(input('enter a number: '))
numbers = list(range(1,num))
# print(numbers)
print(type(numbers))

def summation(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(summation(*numbers)) # unpack

# ======================================================================================
print("_"*50)
# multiply
num = int(input('enter a number: '))
numbers = list(range(1,num))
# print(numbers)
print(type(numbers))

def summation(*args):
    sum = 1
    for i in args:
        sum *= i
    return sum
print(summation(*numbers)) # unpack
