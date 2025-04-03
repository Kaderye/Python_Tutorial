# dictionary comprehension

# example: square of values:   {1: 1, 2: 4, 3: 9, 4: 14}

square_dict = {f"square of {i} ": i**2 for i in range(1, 8)}
print(square_dict)
for p, q in square_dict.items():
    print(f"{p} : {q}")

print("_"*50)

# input: 'kaderye'    count the number of character
string = "kaderye" 
count_char = {char : string.count(char) for char in string}
print(count_char)
for i, j in count_char.items():
    print(f"{i} : {j}")


