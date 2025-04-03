# create a dictionary
student_info = {
    'ID': 1012,
    'Name': 'sojib',
    'Date of birth': 'February 03, 1997',
    'Department': 'CSE',
    'favourite_songs': ['ferary', 'baul'],
    'favourite_movies': ['bibi no 1', 'faluda'],
}

# how to add() data 
student_info['favourite_songs']=['tumi amar jibon', 'o amar bondhu go']
print(student_info)

print("_"*50)
# how to pop() 
popped_item = student_info.pop('favourite_movies')
print(f"Popped item is {popped_item}")
print(student_info)
print(type(popped_item))

print("_"*50)
# popitem() method
poppeditem = student_info.popitem()
print(student_info)
print(poppeditem)
print(type(poppeditem))