# in keyword in sets
set_mixed = {'gk', 33, 5, 66, 'gk', 3.66, -4}
if 'gk' in set_mixed:
    print('present')
else:
    print('not present')

print("_"*50)

# for() loop
for i in set_mixed:
    print(i,end="\t")


# NOTE: set(), remove the duplicate items in a list

print("_"*50)
# union set
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7, 8}
print(set_1 | set_2)

print("_"*50)
# intersection set
print(set_1 & set_2)
