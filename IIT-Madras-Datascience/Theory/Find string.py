# First method of finding a smaller string in a bigger string 
# by if else
x = input() # input like "DS18M0001"
print(x[0] + x[1] == x[0:1+1]  == "DS")

# Second method of finding a smaller string in a bigger string
# by string find()
x = input() # any input that has "DS" in it 
y = x.find("DS")
if y == -1:
    print(False)
else:
    print(True)
    #  OR
print(x.find("DS") > -1)



# Third method of finding a smaller string in a bigger string
# by colon method ( when [:2] is used the character at place 2 isnt 
# included but when [2:] the character at place 2 is also included )
rollno = input()
branch = rollno[:2]
print(branch == 'DS')