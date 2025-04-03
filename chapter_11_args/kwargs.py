# kwargs (keyword arguments)
# **kwargs (double star operator)

# kwargs as a parameter and print as dictionary
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))

func(first_name = 'golam', last_name = 'kaderye')

print("_"*50)
# ===================================================================================
# use loop
def func_1(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")

func_1(first_name= 'golam', last_name= 'kaderye')

print("_"*50)
# ===================================================================================
# pass a name
def func_2(name, **kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")

func_2('shohan', first_name= 'golam', last_name= 'kaderye')

print("_"*50)
# ===================================================================================
# dictionary unpack

def func_3(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys} : {values}")

d = {'name': 'golam', 'height': 5.6}
func_3(**d)

