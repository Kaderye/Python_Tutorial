# function return two values

def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(func(8, 2))
add, multiply = func(8, 2)
print(add)
print(multiply)

print("_"*50)
# function return more values
def func(int1, int2, int3):
    add = int1 + int2 + int3
    multiply = int1 * int2 * int3
    return add, multiply

print(func(8, 2, 3))
add, multiply = func(8, 2, 3)
print(add)
print(multiply)
