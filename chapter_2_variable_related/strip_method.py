name = "   Golam   "
part = "$$$"

# lstrip() function
print(name+part)
print(name.lstrip()+part)
print(name.rstrip()+part)
print(name.strip()+part)

string = "   Go   lam   "
partial = "******"
print(string.strip()+partial)
print(string.replace(" ","")+partial)

print("\n")
# remove space using strip() function
name, character = input("Type your name and a single character: ").split(",")
print(f"The lenght of {name.strip()} is {len(name.strip())}")

print(f"The {character.strip().lower()} is used {name.strip().lower().count(character.strip().lower())} times in {name.strip()}")