"""
Q10) Write a Program to check if the given number is Armstrong number 
     or not.
     Example of Armstrong number are :- 153, 370, 371 etc.


"""

number = int(input("Enter the number: "))
temp = number
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if number == sum:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
