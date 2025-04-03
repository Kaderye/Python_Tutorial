# return vs. print,  which is best for programming

print("use return ")
def add_three_number(number_1, number_2, number_3):
    return number_1+number_2+number_3

print(f"The summation is {add_three_number(6,5,4)}")


print("\n")

print("use print funciton")
def add_three_number(number_1, number_2, number_3):
    print (number_1+number_2+number_3)

add_three_number(6,5,4)