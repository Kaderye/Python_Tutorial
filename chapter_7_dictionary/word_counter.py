# word counter
# example
# kaderye
dict_name = {'k': 1, 'a': 1, 'd': 1, 'e': 2, 'r': 1, 'y': 1, 'e': 2}
print(dict_name)

print("_"*50)
def word_counter(str):
    count = {}
    for i in str:
        count[i] = str.count(i)
    return count

print(word_counter('kaderye'))
