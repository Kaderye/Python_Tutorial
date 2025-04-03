# set: unordered collection of unique items

# create a set
set_number = {3, 1, 7, 3, 3, 6, 9}
print(set_number)
# unordered, unique items (if the item are same and more times but print only one time)

print("_"*50)

# convert set to list
new_list = list(set(set_number))
print(new_list)

print("_"*50)

# convert list to set
list_number = [3, 5, 7, 'sujon', 5, 6, 5]
new_set = set(list_number)
print(new_set)

print("_"*50)

# add a new item in set
print(set_number)
set_number.add(100)
print(set_number)

print("_"*50)

# remove a item in set
print(set_number)
set_number.remove(1)
print(set_number)

print("_"*50)

# discard() is used to remove item
print(set_number)
set_number.discard(9)
print(set_number)

print("_"*50)

# copy() is used to copy
print(set_number)
set_number.copy()
print(set_number)

print("_"*50)

# clear() is used to clear the items in set
print(set_number)
set_number.clear()
print(set_number)

print("_"*50)

# used for()
set_mixed = {'gk', 33, 5, 66, 'gk', 3.66, -4}
for i in set_mixed:
    print(i,end="\t")


