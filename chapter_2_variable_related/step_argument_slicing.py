# string slicing / selecting sub sequences
name = "kaderye"

# positions (index number)
# k = 0 or -7
# a = 1 or -6
# d = 2 or -5
# e = 3 or -4
# r = 4 or -3
# y = 5 or -2
# e = 6 or -1

print(name[2])
print("golam"[2])

# syntax - [start argument : stop argument -1 : step argument]
print(name[0:5])
print(name[0:5:1])
print(name[0:5:2])
print(name[0:5:3])
print(name[0:5:4])
print(name[::2])
print(name[5::-1])
print(name[::-1])

# reverse a string
s_name = input("Enter a string: ")
print(s_name[-1::-1])