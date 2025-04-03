# DATA STRUCTURES

# Topic: List
# ordered collection of items
# you can store anything in lists like int, float, string

# create a list with mixed items
list_1 = [1, 3, "gk", 'pk', -5, '$', "apple"]
print(list_1)
print("_"*50)

# create a list, name is list_number
list_number = [1, 2, 3, 4, 5, 6]
print(list_number)
print(list_number[:])
print("_"*50)

print(list_number[::-1])
print(list_number[-1::-1])
print("_"*50)

print(list_number*3)
print("_"*50)

print(list_number[0])
print(list_number[-1])
print(list_number[:3])
print(list_number[3:])
print(list_number[3:5])
print("_"*50)

# add a new item
list_number[2] = 'gk'
print(list_number)
print(list_number*3)
print("_"*50)

# add a list as a one item
list_number[3] = [45, 22, 44]
print(list_number)
print("_"*50)

# add more items in more positions
list_number[3:] = [45, 22, 44]
print(list_number)
