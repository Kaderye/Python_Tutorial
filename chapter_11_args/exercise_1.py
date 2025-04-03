# define a function
# input: num, iterable (tuple, list) containing numbers as args

# example
# nums = [1,2,3]
# to_power(3, *nums)

# output: list -> [1**3, 8, 27]

# if user didn't pass any args then give a message 'you didn't pass args
# else
# return list
# use list comprehension

# check a list is empty or not
list_numbers = [1,2,3]
if list_numbers:
    print("not empty")
else: 
    print("empty")

print("_"*50)
# ===================================================================================
# check a list is empty or not  with len()
list_numbers = []
if len(list_numbers) > 0:
    print("not empty")
else: 
    print("empty")

print("_"*50)
# ===================================================================================
# check
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else: 
        return "you didn't pass any args"
print(to_power(3,))