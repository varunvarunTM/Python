""" 
Q1) Write a Program to perform string manipulation operations using set 
    of pre-defined functions such as :

a) Find()
b) Upper()
c) Len()
d) Max() and Min()
e) Fetching a specific content from the String 

"""

x = "Hello World"
print("\nString is : ",x)
print("\nFind 'World' in String : ",x.find("World"))
print("\nLength of String is : ",len(x))
print("\nUpper case of String is : ",x.upper())
print("\nLower case of String is : ",x.lower())
print("\nMaximum value of String is : ",max(x))
print("\nMinimum value of String is : ",min(x))
print("\nFetching a specific content from the String : ",x[0:5])
print("\nFetching a specific content from the String : ",x[6:11])
print("\nFetching a specific content from the String : ",x[0:11:2])