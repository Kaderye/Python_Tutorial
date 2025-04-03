# introduction to dictionaries
# it is used due to the limitaions of lists
# lists are not enough to represent real data

# example
# student = ['Sojib', 25, ['bibi no 1', 'dhaka er don'], ['ferari', 'baul']]
# this list contains student name, age,
# favourite movie names, fovourite songs
# you can do this but this is not a good way for programmer

# dictionaries: unordered collection of data in key : value pair

# create a dictionary
student = {'name': 'Sojib', 'age': 25}
print(student)
print(type(student))

print("_"*50)

# another way to create dictionary
employee = dict(name = 'akash', age = 28)
print(employee)
print(type(employee))

print("_"*50)

# how to access data from dictionary
# There is no indexing in dictionary because of unordered collecitons of data
print(employee['name'])
print(employee['age'])

print("_"*50)
# which type of data a dictionary can store?
# anything like numbers, strings, list, dictionary
student_info = {
    'name': 'shohan',
    'age': 26,
    'favourite_movies': ['badsha', 'luttoraj'],
    'favourite_songs': ['baul', 'ferari'],
}
print(student_info['name'])
print(student_info['age'])
print(student_info['favourite_movies'])
print(student_info['favourite_songs'])

"""
print("_"*50)
# dict inside dict
dept_cse ={
    student_1 : {
        'name': 'shohan',
        'age': 26,
        'favourite_movies': ['badsha', 'luttoraj'],
        'favourite_songs': ['baul', 'ferari'],
    },
    student_2 : {
        'name': 'shohan',
        'age': 26,
        'favourite_movies': ['badsha', 'luttoraj'],
        'favourite_songs': ['baul', 'ferari'],
    },
}
print(dept_cse)"
"""

print("_"*50)
# how to add data to empty dictionary
empty_dict = {}
empty_dict['name']= 'sharmin'
print(empty_dict)

empty_dict['age']= 28
print(empty_dict)
