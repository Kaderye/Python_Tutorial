# scope of variable inside and outside functions


x = 12  # global variable

def func():
    global x
    x = 9  # local variable
    return x

print(x)
print(x)
print(func())
print(func())
print(x)
print(x)
