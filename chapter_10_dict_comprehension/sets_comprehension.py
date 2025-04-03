# sets comprehension

# example
# set_numbers = {1, 2, 4, 5, 6}
# output: {1, 4, 9, 16, 25, 36}     square items and unordered
set_numbers = {i**2 for i in range(1, 7)}
print(set_numbers)

print("_"*50)
# another 
names = {'golam', 'kaderye', 'shohan'}
set_names = {i[0] for i in names}
print(set_names)
