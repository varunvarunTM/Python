print("")

#ARITHEMATIC [ + , - , * , / , // , % , ** ]

print("addition :",7+3)
print("subtraction :",7-3)
print("multiplication :",7*3)
print("division :",7/3)  #Results in float value
print("floor/integer division :",7//3)
print("modulus :",7%3)
print("exponentiation :",7**3)

#RELATIONAL [ > , < , >= , <= , == , != ]
#data types for these is boolean

print("")

#LOGICAL [ and , or , not ]
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("")
print(not True)
print(not False)

print("")

#string comparison
print("apple" < "banana" )
print("abcd" > "abcde")

print("")

#string indexing
s = "python"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])

print("")

for i in range(0,6):
    print(s[i])

print("")

print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])
print(s[-5])
print(s[-6])

print("")

#search engine

print("alpha" in "a variable name can only contain alpha-numeric characters and underscores")
print("alpha" in "a variable name must start with a letter  or the underscore character")

print("")

#String Methods

x = "pytHoN sTrIng mEthOdS\n"
print(x)
print("lower = ",x.lower())
print("upper = ",x.upper())
print("capitalize = ",x.capitalize())
print("title = ",x.title())
print("swapcase = ",x.swapcase())

print("")

x = "python"
print(x.islower())
x = "Python"
print(x.islower())
x = "PYTHON"
print(x.isupper())
x = "PYThON"
print(x.isupper())
x = "Python Expert"
print(x.istitle())
x = "PYthon Expert"
print(x.istitle())

print("")

x = "123"
print(x.isdigit())
x = "123abc"
print(x.isdigit())
x = "abc"
print(x.isalpha())
x = "abc123"
print(x.isalpha())
x = "123abc"
print(x.isalnum())
x = "123abc*#"
print(x.isalnum())

print("")

x = "-----Python-----"
print(x.strip("-"))
print(x.lstrip("-"))
print(x.rstrip("-"))

print("")

x = "Python "
print(x.startswith("P"))
print(x.startswith("p"))
print(x.endswith("n"))
print(x.endswith("N"))


print("")

x = "Python String Methods"
print(x.count("t"))
print(x.count("s"))
print(x.index("t"))
print(x.index("s"))
x = x.replace("S","s")
x = x.replace("M","m")
print(x)
print(x.split(" ") , x.split())
print(x.split()[1])

print("")

#string character positions

string = "abcdefghijklmnopqrstuvwxyz"
i = 23
print(string[-2])
print(string[-1])
print(string[0])
print(string[1])
print(string[(i)%26])
print(string[(i+1)%26])
print(string[(i+2)%26])
print(string[(i+3)%26])
print(string[(i+4)%26])
print(string[24])
print(string[25])

print("")

#                                math.ceil() Function
# In Python, the method ceil(x) returns the smallest integer greater than or equal to x.
# It is called the ceiling value of x.

import math
x = 3.5
print(math.ceil(x))

#                                math.floor() Function
# The math.floor() function produces the greatest integer not greater than x.
# If the number is already an integer, it returns the same number.

import math
x = 3.5
print(math.floor(x))

print("")

# To split string when length of input string is equal to the number of variables 
a,b,c,d = "1234" # OR input() with length = 4
print(a) # 1
print(b) # 2
print(c) # 3
print(d) # 4

# makes a string with characters at place difference = 2 from position 0 to less than 10
alphabets = 'abcdefghijklmnopqrstuvwxyz'
even = alphabets[0: 10: 2]
print(even)