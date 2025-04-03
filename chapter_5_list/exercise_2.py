# define a function which will take list as a argument and this function
# will return a reserved lis

# example: 
# [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
# note: reverse method or [::-1]
# but try to do this with the help of append and return method

numbers = [1, 2, 3, 4, 5]
print(numbers)
def reverse_numbers(rn):
    rn.reverse()
    return rn

print(reverse_numbers(numbers))