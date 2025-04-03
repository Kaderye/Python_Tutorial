# create a list
country_names = ['Bangladesh', 'Japan', 'Nepal', 'Bhutan', 'Canada', 'England', 'Bangladesh', 'Canada', 'Bangladesh']

# how many times used Bangladesh
print(country_names.count('Bangladesh'))
print(country_names.count('Canada'))
print("_"*50)

# sort() used to sorting the items
numbers = [23, 3, 77, 1, 5, 9]
numbers.sort()
print(numbers)
country_names.sort()
print(country_names)
print("_"*50)

# sorted() used for sorting
sorted(country_names)
print(country_names)
sorted(numbers)
print(numbers)
print("_"*50)

# reverse() used to reverse a list
numbers.reverse()
print(numbers)
country_names.reverse()
print(country_names)
print("_"*50)

# copy() used for copy a list
numbers.copy()
print(numbers)
print("_"*50)

# clear() used to empty a list
numbers.clear()
print(numbers)
print("_"*50)

