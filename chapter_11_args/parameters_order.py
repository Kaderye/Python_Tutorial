# functions with all parameter

# PADK: parameters, args, default parameters, kwargs

# default parameters
def func(name= 'golam', age=28):
    print(f"name : {name}")
    print(f"age : {age}")

func('kaderye', 26)

print("_"*50)
# ===============================================================================
# normal parameters
def func(name, *args, last_name= 'kaderye', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('golam', 1,2,3, a=1, b=2)
