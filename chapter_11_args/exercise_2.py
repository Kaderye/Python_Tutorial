# define a function
# names = ['golam', 'kaderye']


# print(func(names))
# print(func(names, reverse_str = True))

# input a string list 
# output_1:  the first letter will be capital of each values
# output_2: first reverse each values with the first letter is capital

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
    
names = ['golam', 'kaderye']
print(func(names))
print(func(names, reverse_str = True))