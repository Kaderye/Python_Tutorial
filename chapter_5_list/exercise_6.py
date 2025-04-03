# find the list numbers in a list
# example
# input: [1, 2, 3, [4, 5]] output: 1
# input: [1, 2, 3, [4, 5], [6, 7]] output: 2

numbers = [1, 2, 3, [4, 5], [6, 7]]
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

print(f"The number of sublist is {sublist_counter(numbers)}")