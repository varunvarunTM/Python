upper = 100

print("Prime numbers between", 0 , "and", upper, "are:")

for num in range(0, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print("|",num,"|")