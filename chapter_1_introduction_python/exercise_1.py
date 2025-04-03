
# Print the follwing lines:
# this is \\ double backslash
# these are /\/\/\/\ mountains
# he is   awesome (use escape sequence insteed of manual spaces)
# \" \n \t \' (print this as an output)

print("\n")
print("this is \\\\ double backslash")
print("these are /\\/\\/\\/\\ mountains")
print("he is\tawesome")
print(" \\\" \\n \\t \\\' ")

# shortcut way to present escape sequence as nortmal text
print(r"Line A \n Line B")
print(r"\n")
print(r" \" \n \t \' ")

# print emoji
# U+1F600 use for grinning face 
# replace + by 000 and add \ before unicode
# Link for unicode: https://unicode.org/emoji/charts/full-emoji-list.html
print("\U0001F600")
print("\U0001F604")
print("\U0001F60D")