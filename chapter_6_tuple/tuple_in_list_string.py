# create a tuple using range() function
numbers = tuple(range(1, 6))
print(numbers)
print(type(numbers))

print("_"*50)
# convert tuple to string
digits = str((1, 2, 3, 4, 5))
print(digits)
print(type(digits))

print("_"*50)
# convert tuple to list
names = list(('gk', 'pk', 'rk'))
print(names)
print(type(names))

print("_"*50)
# convert list to tuple
a_list = tuple([1, 2, 3, 4, 5])
print(a_list)
print(type(a_list))

print("_"*50)
# convert list to string
b_list = str([5, 6, 2, 3, 4, 5])
print(b_list)
print(type(b_list))

print("_"*50)
# convert string to tuple
a_tuple = tuple("[1, 2, 3, 4, 5]")
print(a_tuple)
print(type(a_tuple))

print("_"*50)
# convert list to string
b_tuple = list("[5, 6, 2, 3, 4, 5]")
print(b_tuple)
print(type(b_tuple))
