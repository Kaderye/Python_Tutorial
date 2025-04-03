# is or  == used to compare lists

country_list_1 = ['Bangladesh', 'Japan', 'Nepal', 'Bhutan']
country_list_2 = ['Canada', 'England', 'Bangladesh', 'Canada', 'Bangladesh']
country_list_3 = ['Bangladesh', 'Japan', 'Nepal', 'Bhutan']
country_list_4 = ['Japan', 'Nepal','England', 'Bangladesh']

print(country_list_1 == country_list_2) # are not same
print(country_list_1 == country_list_3) # same items
print(country_list_1 is country_list_4) # not same location
print(country_list_1 is country_list_3) # not same location