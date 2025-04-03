# fibonacci series
# 0 1   1   2   3   5   8   13  21  34

def fibonacci_series(number):
    first_number = 0
    second_number = 1
    if number == 1:
        print(first_number)
    elif number == 2:
        print(first_number, second_number, end="\t")
    else:
        print(first_number, second_number, end="\t")
        for i in range(number-2):
            temp = first_number + second_number
            first_number = second_number
            second_number = temp;
            print(second_number, end="\t")

fibonacci_series(10)