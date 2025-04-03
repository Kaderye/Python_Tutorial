# define a function then filter odd and even

# example
# input: list[1,2,3,4,5,6,7,8,9]
# output: [[1,3,5,7,9], [2,4,6,8]]

numbers = [1,2,3,4,5,6,7,8,9]
def create_list(l):
    even_numbers = []
    odd_numbers = []
    for i in l:
        if i%2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    output = [odd_numbers, even_numbers]
    return output

print(create_list(numbers))

