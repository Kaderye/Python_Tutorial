# exercise
# define a function that take list of strings
# list containing reverse of every string

# NOTE: use list comprehension

# example
# list_string = ['shohan', 'rajon', 'mijan', 'gk']
# reverse_string = ['nahohs', 'nojar', 'najim', 'kg']

# ==============================================================================================================
# create a list using list_func() function
# item_number = int(input('enter the item numbers: '))
# def list_func(l):
#     create_list = []
#     for i in range(l):
#         items = input(f'enter item number {i+1}: ')
#         create_list.append(items)
#     return create_list
   
# print(list_func(item_number))

# ==============================================================================================================
# reverse a list items using list_func()

# item_number = int(input('enter the item numbers: '))
# def list_func(l):
#     create_list = []
#     for i in range(l):
#         items = input(f'enter item number {i+1}: ')
#         create_list.append(items[::-1])
#     return create_list
   
# print(list_func(item_number))

# ==============================================================================================================
# revese a list items
# item_number = ['golam', 'kaderye', 'shohan']
# def list_func(l):
#     return [i[::-1] for i in l]
   
# print(list_func(item_number))

# ==============================================================================================================
# revese a list items
# item_number = int(input('enter the number of items: '))
# create_list = []
# for i in range(item_number):
#     items = input(f'enter item number {i+1}: ')
#     create_list.append(items)
# print(f"The create list is {create_list}")

# def list_func(create_list):
#     return [i[::-1] for i in create_list]
   
# print(f"The reverse items of list is {list_func(create_list)}")

# ==============================================================================================================
# revese a list items
item_number = int(input('enter the number of items: '))

def list_func(item_number):
    create_list = [input(f'enter item number {i+1}: ') for i in range(item_number)]
    print(f"The create list is {create_list}")
    return [i[::-1] for i in create_list]
   
print(f"The reverse items of list is {list_func(item_number)}")