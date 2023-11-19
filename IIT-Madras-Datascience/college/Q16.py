"""
Q16) Write a Program to create and display the content of the tuple. 
     Initialize the tuple with the name of the cities.
     Display content of the tuple along with name/index positions of the cities.

"""

cities = ("Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad")
print("Cities in the tuple:")
for index, city in enumerate(cities):
    print(f"Index {index+1}: {city}")