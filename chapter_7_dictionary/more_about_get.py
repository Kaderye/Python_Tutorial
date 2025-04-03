# more about get(), two same keys in dictionaries
dict_d1 = {'name': 'gk', 'height': 5.6, 'weight': 68}
print(dict_d1.get('name')) # output: gk
print(dict_d1.get('names')) # output: False
print(dict_d1.get('names', 'Not found')) # output: Not found

print("_"*50)
# what happend
dict_d2 = {'name': 'gk', 'height': 54, 'height': 68}
print(dict_d2) # here overrite 




