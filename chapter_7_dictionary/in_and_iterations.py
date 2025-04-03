# create a dictionary name is student_info
student_info = {
    'ID': 112,
    'name': 'rajon',
    'department': 'EEE',
    'Batch': 27
}

# check a key is present or not in dictionary
if 'Batch' in student_info:
    print('present')
else:
    print("not present")

print("_"*50)
# check value is present or not in dictionary
if 27 in student_info.values():
    print('present')
else:
    print("not present")


print("_"*50)
# check value is present or not in dictionary
if '27' in student_info.values():
    print('present')
else:
    print("not present")


print("_"*50)
# keys method
for i in student_info:
    print(student_info[i])


print("_"*50)
# loops in dictionaries
for i in student_info:
    print(i)

print("_"*50)
# loops in dictionaries
for i in student_info.values():
    print(i)

print("_"*50)
# values method
student_info_values = student_info.values()
print(student_info_values)
print(type(student_info_values))

print("_"*50)
# keys method
student_info_keys = student_info.keys()
print(student_info_keys)
print(type(student_info_keys))

print("_"*50)
# keys method
for i, j in student_info.items():
    print(f" Key is {i} and it\'s {j}")

