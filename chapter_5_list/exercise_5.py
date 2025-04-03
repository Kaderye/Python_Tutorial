# common elements finder function
# define a function which take 2 lists as input and return a list
# which contains common elements of both lists

# example
# input: list_1 = [3, 5, 7, 9, 10]
#        list_2 = [1, 2, 3, 4, 5]
# output: [3, 5]

list_1 = [3, 5, 7, 9, 10]
list_2 = [1, 2, 3, 4, 5]
def common_items(l1, l2):
    common = []
    for i in l1:
        for j in l2:
            if i == j:
                common.append(i)
    return common

print(common_items(list_1, list_2))
print("_"*50)

# another way
list_1 = [3, 5, 7, 9, 10]
list_2 = [1, 2, 3, 4, 5]
def common_items(l1, l2):
    common = []
    for i in l1:
        if i in l2:
            common.append(i)
    return common

print(common_items(list_1, list_2))