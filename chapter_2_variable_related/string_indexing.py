# string indexing
name = "kaderye"
# positions (index number)

# k = 0 or -7
# a = 1 or -6
# d = 2 or -5
# e = 3 or -4
# r = 4 or -3
# y = 5 or -2
# e = 6 or -1

# print the 5th index character of name 
print(name[5])
print(name[-1])

print("\n")

# print all character of name sting
for i in name:
    print(i)


#  count lenght
count = 0
for i in name:
    count = count + 1
print(f"The lenght of {name} is {count}")

# another way
print(f"The lenght of {name} is {len(name)}")