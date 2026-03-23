# Program to check if a variable is a letter or a number

value = input("Enter a value: ")

if value.isalpha():
    print("It's a letter")
elif value.isdigit():
    print("It's a number")
else:
    print("It's neither a letter nor a number")