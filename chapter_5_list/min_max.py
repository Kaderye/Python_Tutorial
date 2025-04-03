# min() and max() function

numbers = [1, 2, 3, 4, 5, 6, 7]
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")

def difference_max_min(l):
    return max(numbers) - min(numbers)

print(f"The differnce between {max(numbers)} and {min(numbers)} is {difference_max_min(numbers)}")
