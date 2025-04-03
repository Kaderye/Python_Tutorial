# Ask user input a name and print the last character
name = input("Type your name: ")

def last_character(name):
    return name[-1]

print(f"The last character of \'{name}\' is {last_character(name)}")