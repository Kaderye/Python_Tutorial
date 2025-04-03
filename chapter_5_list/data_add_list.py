# add item in list using append()
# append() add item in the last postion in list
name_list_1 = ['gk','pk','mk']
print(name_list_1)
name_list_1.append('rk')
print(name_list_1)
print("_"*50)

# add item in list using insert()
# insert() add item in any position in list
name_list_2 = ["arab", "sojib", 'akash']
print(name_list_2)
name_list_2.insert(1, 'sujon')
print(name_list_2)
name_list_2.insert(3, 'riaz')
print(name_list_2)
print("_"*70)

# concate two or more lists
name_list = name_list_1 + name_list_2
print(name_list)
print("_"*70)

# extend() like as concate
name_list_2.extend(name_list_1)
print(name_list_2)
print(name_list_1)
print("_"*100)

# extend() replace by append() what happend?
name_list_2.append(name_list_1)
print(name_list_2)
print(name_list_1)

