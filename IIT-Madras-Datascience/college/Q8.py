"""
Q8) Write a Program that receives marks of a students for a subject as 
    input and assign the grades A||B||C||D||E||F 

"""

marks = int(input("Enter the marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 50:
    print("Grade E")
else:
    print("Grade F")
