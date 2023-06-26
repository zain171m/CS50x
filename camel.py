camel = input("camelCase: ")
print("snake_case: ",end = "")
for letter in camel:
    if letter.isupper():
        letter = letter.lower()
        print("_" + letter, end = "")
    else:
        print(letter, end = "")
print()
