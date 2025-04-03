"""
Problem: Write a program to Find the Largest Number Among Three Numbers
"""


# find the greater number
# def greater(a,b):
#     if a>b:
#         return a
#     return b
# print(greater(6,9))



# find the greatest number
# def greatest(a,b,c):
#     if a>b and b>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(greatest(5,9,3))


# function inside function
# greater(a,b)       -> a or b
# greater(a or b, c) -> greatest

def greater(a,b):
    return max(a,b)

def new_greatest(a,b,c):
    big = greater(a,b)
    return greater(big,c)
    # return greater(greater(a,b),c)

print(new_greatest(6,8,23))

