# *operator
# *args

# add two numbers using a function
def add(a,b):
    return a+b
print(add(7,10))

# ======================================================================================================
print("_"*50)
# if we want to add more numbers then we used *args
def summation(*args):
    print(args)
    print(type(args))

summation(1,2,3,4,5)

# ======================================================================================================
print("_"*50)
# another example
def total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(total(1,2,3,4,5))

# ======================================================================================================
print("_"*50)
