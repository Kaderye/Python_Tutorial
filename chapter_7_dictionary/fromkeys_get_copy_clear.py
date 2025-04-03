# fromkeys() is used to create dictionary
# if we want to store same values in different keys in dictionary then we used fromkeys()

#exmaple:
# dict_d = {'name': 'unknown', 'age': 'unknown', 'height': 'unknown}

dict_d = dict.fromkeys(['name', 'age', 'height'], 'unknown')  # used list
print(dict_d)

print("_"*50)
# another 
dict_d = dict.fromkeys(('name', 'age', 'height'), 'unknown')  # used tuple
print(dict_d)

print("_"*50)
# another 
dict_d = dict.fromkeys(('abcd'), 'unknown')  # used string
print(dict_d)

print("_"*50)
# another 
dict_d = dict.fromkeys(range(1,5), 'unknown')  # used range()
print(dict_d)

print("_"*50)
# another 
dict_d = dict.fromkeys(['name', 'age', 'height'], ['abc', 'def'])
print(dict_d)


print("_"*50)
# =================================================================================================
# get() is used to check a key in present or not in a dictionary 
dict_dic = {
    'name': 'kaderye',
    'address': 'dhaka',
    'study': 'cse',
}
print(dict_dic.get('address'))

print("_"*50)
# another way
print(dict_dic['name'])

print("_"*50)
# another way
if 'study' in dict_dic:
    print('present')
else: 
    print('not present')

print("_"*50)
# another way
if dict_dic.get('names'):
    print('present')
else:
    print('not present')

# NOTE: if None  -> false else -> true

# =================================================================================================
print("_"*50)

# clear() is used to clear dictionary
dict_dic.clear()
print(dict_dic)

# =================================================================================================
print("_"*50)

# copy() is used to copy a new dictionary from the old dictionary
copy_dict = {'name': 'gk', 'height': 5.6, 'weight': 68}
new_dict = copy_dict.copy()
print(copy_dict)
print(new_dict)

print("_"*50)
# NOTE: if we write  copy_dict = new_dict that means it's equal but not copy here
print(new_dict.popitem())
print(new_dict)
print(copy_dict)

print(copy_dict is new_dict) # check copy_dict is not equal to new_dict when use = operator
