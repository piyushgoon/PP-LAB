def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower

string = input("Enter a string: ")
upper, lower = count_case(string)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")