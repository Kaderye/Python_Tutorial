# dictionary comprehension with if else

# example:
# dict = {1: 'odd', 2: 'even'}
numbers = {i:('even' if i%2 == 0 else 'odd') for i in range(1, 6)}
print(numbers)

for i, j in numbers.items():
    print(f"{i} : {j}")

