# take two comma separated inputs from user
# 1. user's name
# 2. a single character

# Output: 2 print lines
# 1. user's name length
# 2. count the character that user inputed (Hints: case insensitive count)

name, character = input("Type your name and a single character: ").split(",")
print(f"The lenght of {name} is {len(name)}")
# character is casesensitive
print(f"The {character} is used {name.count(character)} times in {name}")
# this is the wright way
print(f"The {character} is used {name.lower().count(character.lower())} times in {name}")