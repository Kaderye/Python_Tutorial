# replace() function
# find() function

string = "bangladesh is a beautifull country in south asia and it is really wonderful"
print(string.replace(" ","_"))
print(string.replace("is","was", 1))


# find() method
print(string.find("is"))
print(string.find("is", 15))

is_pos = string.find("is")
print(string.find("is",is_pos+1))
