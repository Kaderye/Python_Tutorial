# define a function that take list of words as argument and
# return list with reverse of every element in that list

# example
# ['akash', 'batash', 'pabna'] -> ['hsaka', 'hsatab', 'anbap']


strings = ['akash', 'batash', 'pabna']
def reverse_list_items(rli):
    items = []
    for i in rli:
        items.append(i[::-1])
    return items
print(reverse_list_items(strings))
