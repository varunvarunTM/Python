"""
Q4) Write a Program that receive input from the user to calculate the Area 
    of Triangle

"""

side_a = int(input("Enter the value of side a: "))
side_b = int(input("Enter the value of side b: "))
side_c = int(input("Enter the value of side c: "))
s = (side_a + side_b + side_c) / 2
area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5
print("Area of Triangle is: ", area)