# create a 2d list inside list
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbers)
print(numbers[1])
print("_"*50)

# print using loop
for i in numbers:
    print(i)

print("\n"+"_"*50)

# print all items
for i in numbers:
    for j in i:
        print(j, end="\t")

print("\n"+"_"*50)

# print the all items of index[1]
print(numbers[2][1])

print(type(numbers))

