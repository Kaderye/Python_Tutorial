# ask user a number to create a list
number = list(range(1,11))

# as a normal style
new_list = []
for i in number:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)

print("_"*50)
# using a function
def new_list(number):
    return [i*2 if i%2 == 0 else -i for i in number]

print(new_list(number))