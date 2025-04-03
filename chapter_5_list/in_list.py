# in keyword is used to check a item is present or not in a list 
number = [1, 2, 3, 4, 5, 6, 7]
check_number = int(input("enter a number: "))

if check_number in number:
    print(f"{check_number} is present")
else:
    print(f"{check_number} is not present")
