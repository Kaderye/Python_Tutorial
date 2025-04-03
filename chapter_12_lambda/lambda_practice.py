# practice : lambda

def is_even(n):
    if n%2 == 0:
        return True
    return False

print(is_even(7))

print("_"*50)
# ==================================================================
# use lambda
check_even = lambda n : n%2 == 0
print(check_even(7))

print("_"*50)
# ==================================================================
# print the last character
last_character = lambda c : c[-1]
print(last_character("kaderye"))

print("_"*50)
# ==================================================================
# use lambda
check = lambda s : len(s) > 3
print(check("golam"))

