# crate a list

# numbers = list(range(1, 11))
# print(numbers)

number = int(input('enter a number: '))
even_number_list = [i for i in range(1,number) if i%2 == 0]
print(even_number_list)
odd_number_list = [i for i in range(1, number) if i%2 != 0]
print(odd_number_list)
