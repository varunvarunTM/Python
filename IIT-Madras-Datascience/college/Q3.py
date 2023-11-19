"""
Q3) Write a Program that receive a number as input from user and returns 
    if it odd or even number.

"""

x = int(input("\nEnter a number : "))
if x%2 == 0:
    print("\n",x," is an even number.")
else:
    print("\n",x," is an odd number.")


# shortened

print("\n",x," is an even number.") if x%2 == 0 else print("\n",x," is an odd number.")