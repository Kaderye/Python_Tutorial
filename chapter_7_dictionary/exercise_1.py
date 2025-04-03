# exercise
# define a function that takes a number (N)
# return a dictionary containing cube of numbers from 1 to N

# example:
# cube_number(4)
# {1: 1, 2: 8, 3: 27, 4: 64}

def cube_number(number):
    cube = {}
    for i in range(1, number):
        cube[i] = i**3
    return cube

print(cube_number(5))