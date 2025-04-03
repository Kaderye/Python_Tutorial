# in keyword
# if with in

name = input("Type your name: ")
character = input("Type a single character: ")

if (character in name):
    print(f"{character} is present in {name}")
else:
    print(f"{character} is not present in {name}")
