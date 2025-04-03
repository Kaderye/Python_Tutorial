# WATCH BANGLA MOVIE
# Ask user's name and age
# if user's name start with (a or A) and age is above 18 then
# print "You can watch bangla movie"
# else print "Sorry, you can not watch bangla movie"

name, age = input("Enter your name and age ").split(",")
# print(name)
# print(age)

# name = input("Type your name: ")
# age = int(input("Enter your age: "))

if ((name[0].strip()=='a' or name[0].strip()=='A') and int(age) > 18):
    print("You can watch bangla movie")
else:
    print("Soryy, you can not watch bangla movie")