# generate lists with range function
numbers = list(range(1,10))
print(numbers)
print("_"*50)

# about pop() function
numbers.pop()
print(numbers.pop()) # show the pop() number
print(numbers)
print("_"*50)

#
print(numbers.index(1))
# print(numbers.index(1, 3))
print("_"*50)

# pass list to a function
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))

print("_"*50)

# another pass list to a function
values = list(range(5,15))
print(values)
print("_"*50)

def negative_values(input_values):
    negative = []
    for i in input_values:
        negative.append(-i**2)
    return negative

print(negative_values(values))