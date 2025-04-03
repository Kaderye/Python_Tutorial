# all are same problems
# problem 1: print the summation of N natural numbers
# problem 2: Ask a user for N natural numbers
# problem 3: print the summation from 1 to N 

n_natural_number = int(input("Enter the nth natural number: "))

sum = 0
for i in range(n_natural_number+1):
    sum = sum + i
    i += 1

print(f"The summation from 1 to {n_natural_number} is {sum}")
