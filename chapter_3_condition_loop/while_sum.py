# problem: print the summation from 1 to 100 (or any number)

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the end number: "))

i = start_number
sum = 0
while(i <= end_number):
    sum = sum + i
    i = i + 1
print(f"The summation from {start_number} to {end_number} is {sum}")

