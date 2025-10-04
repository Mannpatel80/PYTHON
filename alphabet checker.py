# Program to check if a character is an alphabet manually

ch = input("Enter a character: ")

if len(ch) == 1:   # make sure only one character is entered
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        print("The character is an alphabet.")
    else:
        print("The character is not an alphabet.")
else:
    print("Please enter only one character.")
