# exercise

# numbers to string using a function

# example
# input: [True, False, [1,2,3], 5, 5.5, 9]
# output: ['5', '5.5', '9']

input_list = [True, False, [1,2,3], 5, 5.5, 9]
def number_to_string(input_list):
    return [str(i) for i in input_list if (type(i)==int or type(i)==float)]

print(number_to_string(input_list))




# another 
output_list_1 = [str(i) for i in input_list if (type(i)!=int and type(i)!=float)]
print(output_list_1)

