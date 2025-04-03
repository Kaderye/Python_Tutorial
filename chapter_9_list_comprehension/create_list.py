# create list as normal
# user_info = input('Enter items separated by space: ').split()
# print(user_info)

# =====================================================================================================
# another as normal
# user_in = input('Enter items separated by comma: ').split(',')
# print(user_in)

# =====================================================================================================
# get list as input using a loop
# new_list = []
# number = int(input('Enter a number: '))
# for i in range(number):
#     item = input(f'enter item number {i+1}: ')
#     new_list.append(item)

# print(f"The list is {new_list}")

# =====================================================================================================
# get list as input using map()
# user_item = list(map(int, input('enter items separated by space: ').split()))
# print(user_item)

# =====================================================================================================
# using list comprehension for concise input
# number = int(input('enter the number of items: '))
# # list_new = [i for i in range(number)]
# list_new = [input(f'enter item number {i+1}: ') for i in range(number)]
# print(list_new)

# =====================================================================================================
# accepting a nested list input
user_input = [i.split(',') for i in input('enter items using comma and semicolon: ').split(';')]
print(user_input)

