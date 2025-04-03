# tuple data structure
# tuple can store any data type
# most important tuples are immutable
# immutable: once tuple is created you can not update
# data inside tuple
# tuple are faster than list
# methods
# count, index, len(), slicing

# example
# tuple_1 = ('rahim', 'karim', 'abbas', 'rajon')
# no append, no insert, no pop, no remove

days_name = ('Saturday', 'Sunday', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday')

print(days_name)
print(days_name[:])
print(len(days_name))
print("_"*50)

print(days_name[::-1])
print(days_name[-1::-1])
print("_"*50)

print(days_name*2)
print("_"*50)

print(days_name[0])
print(days_name[-1])
print(days_name[:3])
print(days_name[3:])
print(days_name[3:5])