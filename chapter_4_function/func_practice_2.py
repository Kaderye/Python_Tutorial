# check a number is even or odd

number = int(input("Enter an integer number: "))
def check_even_odd(number):
    if number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

check_even_odd(number)




# another style
# number = int(input("Enter an integer number: "))
# def check_even_odd(number):
#     if number%2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"
# print(check_even_odd(number))



# # another style
# number = int(input("Enter an integer number: "))
# def check_even_odd(number):
#     if number%2 == 0:
#         return "EVEN"
#     return "ODD"
# print(check_even_odd(number))