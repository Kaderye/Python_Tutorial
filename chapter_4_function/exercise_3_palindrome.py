# define is_palindrome function that take one word in string as input
# and return True if it is plaindrome else return False

# plaindrome : word that reads same backwards as forwards

# Example: 
# is_plaindrome("level") or ("radar") -> True
# is_plaindrome("abba") -> True
# is_plaindrome("apple") -> False

# logic (algorithm)
# step-1: reverse the string
# step-2: compare reversed string with original string

original_string = input("Enter a string : ")
print(f"The original string is \'{original_string}\'")

def is_palindrome(original_string):
    reversed_string = original_string[-1::-1]
    print(f"The reversed string is \'{reversed_string}\'")
    if original_string == reversed_string:
        return True
    return False
    
print(f"It is {is_palindrome(original_string)}")



# another simple way
def is_palindrome(original_string):
    return original_string == original_string[::-1]

print(f"It is {is_palindrome(original_string)}")