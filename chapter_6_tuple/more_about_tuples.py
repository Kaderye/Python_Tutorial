# create a tuple
friend_names = ('shohan', 'rajon', 'arif', 'tuhin', 'shovon', 'akash')

# looping in tuples
for i in friend_names:
    print(i, end="\t")

print("\n")
print("_"*50)

# while loop
i = 0
while(i<len(friend_names)):
    print(friend_names[i],end="\t")
    i += 1

print("\n")
print("_"*50)
# create a function
def friends(name):
    for i in name:
        print(i,end="\t")

friends(friend_names)

print("\n")
print("_"*50)
# tuple with one element
number = (4)
number_tuple = (10,)
word = ('south')
word_tuple = ('south',)
print(type(number))
print(type(number_tuple))
print(type(word))
print(type(word_tuple))

print("_"*50)
# tuple without parenthesis
car = 'BMW', 'Ferari', 'Marcedis'
print(type(car))

print("_"*50)
# tuple unpacking
names = ('sojib', 'akram', 'sanjida')
friend_1, friend_2, friend_3 = (names)
print(friend_1)
print(friend_2)
print(friend_3)

print("_"*50)
# list inside tuples
sports = ('football', ['cricket', 'hocky', 'chess'])
print(type(sports))
print(sports)

sports[1].pop()
print(sports)

sports[1].append('playing card')
print(sports)

# min(), max(), sum() used in tuple
numbers = (1, 2, 3, 4, 5)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
