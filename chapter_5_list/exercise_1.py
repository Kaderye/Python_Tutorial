# define a function which will take list containing numbers as input
# and return list containing square of every elements

# example: 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# square_list(numbers) -> return -> [1, 4, 9, 16, 25, 36, 49, 64]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers)
def square_list(numbers):
    number = []
    for i in numbers:
        number.append(i**2)
    return number

print(square_list(numbers))