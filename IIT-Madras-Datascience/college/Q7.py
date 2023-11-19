"""
Q7) Write a Program to check if the input string is Palindrome or not

"""

string = input("Enter the string: ")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")