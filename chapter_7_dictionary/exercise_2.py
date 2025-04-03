# exercise
# Ask user to input all the keys values and create a dictionary

student = {}
name = input('Enter your name: ')
age = int(input('Enter your age: '))
favourite_movies = input('Enter your favourite movies separeted by comma: ').split(',')
favourite_songs = input('Enter your favourite songs separeted by comma: ').split(',')

student['name'] = name
student['age'] = age
student['favourite_movies'] = favourite_movies
student['favourite_songs'] = favourite_songs

print(student)

print("_"*50)
# use for() to print
for i, j in student.items():
    print(f"{i} : {j}")