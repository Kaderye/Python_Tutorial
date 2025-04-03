# create a dictionary
student_info = {
    'ID': 1012,
    'Name': 'sojib',
    'Date of birth': 'February 03, 1997',
    'Department': 'CSE',
    'favourite_songs': ['ferary', 'baul'],
    'favourite_movies': ['bibi no 1', 'faluda'],
}
print(student_info)
print("_"*50)

another_info = {
    'grade': 'A',
    'cgpa': 3.57,
}

student_info.update(another_info)
print(student_info)

# important note: if there are same key in both dictionary
# then replace the name value by the another dictionary

print("_"*50)
# if we used empty dict as like below then print None
print(student_info.update({}))
