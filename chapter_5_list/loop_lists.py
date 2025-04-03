# create a list
numbers = [3, 6, 1, 99, 33, 2, 5, 3]
print(numbers)
print("_"*50)

# use for loop
for i in numbers:
    print(i, end="\t")

print("\n")
print("_"*50)

# use while loop
i = 0
while i<len(numbers):
    print(numbers[i], end="\t")
    i += 1