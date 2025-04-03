# Ask user for name
# Example: University
# print count the each words
# output: 
# u : 1
# n : 1
# i : 2
# v : 1
# e : 1
# r : 1
# s : 1
# t : 1
# y : 1

name = input("Type a name: ")

temp_var = ""
i = 0
while(i<len(name)):
    if (name[i] not in temp_var):
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
