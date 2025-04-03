# pop() used to delete the last item in list
name = ['akash', 'batash', 'monju', 'akash', 'ronju', 'pial', 'robi']
print(name)
name.pop()  # delete the last item by default
print(name)
print("_"*50)

# delete any item from any position
name.pop(1) # delete the 1th postion item
print(name)
print("_"*50)

# del used to delete item from any position
del name[3]
print(name)
print("_"*50)

# remove() used to delete item by item 
# when item is double or more then delete the first item
name.remove('akash')
print(name)
