# list comprehension: it's help to create a list in one line

# create a list of squares from 1 to 7
squares = []
for i in range(1, 8):
    squares.append(i**2)

print(squares)

print("_"*50)

# create a list used list comprehension
number_list = [i for i in range(1,8)]
print(number_list)

print("_"*50)

# create a list used list comprehension
n_list = []
for i in range(1, 6):
    n_list.append(i)

print(n_list)

print("_"*50)

# create a list used list comprehension
multiply_list = [i*i for i in range(1,8)]
print(multiply_list)

print("_"*50)

# create a list used list comprehension
squares_list = [i**2 for i in range(1,8)]
print(squares_list)

print("_"*50)

# create a list used list comprehension
cube_list = [i**3 for i in range(1,8)]
print(cube_list)

print("_"*50)

# create a list used list comprehension
negative_list = [-i for i in range(1,8)]
print(negative_list)

print("_"*50)

# create a list used list comprehension
n_list = []
for i in range(1, 6):
    n_list.append(-i)

print(n_list)

print("_"*50)
# another example
# names = ['shohan', 'rajon', 'milon', 'jodu']
# output: new_names = ['s', 'r', 'm', 'j']
names = ['shohan', 'rajon', 'milon', 'jodu']
new_names = []
for i in names:
    new_names.append(i[0])
print(new_names)

print("_"*50)
# another example
new_names_2 = [i[0] for i in names]
print(new_names_2)
