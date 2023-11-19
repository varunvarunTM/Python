n=str(input("\nHello, enter your name please : "))

while True:

 if(n == "varun"):
      print("hi", n ,"sir")
      break

 else:
      print("hi user", n )
      break

while True:

 if(n == "varun"):
      n=n + " sir"
      break
     
 else:
      n=n
      break

p=str(input("\nwhich place are you currently staying in? : "))

print("\nSo", n ,"how is the weather in", p , "? : " )

s=str(input())

a=int(input("\nby the way, what is your age : "))

print("\ngood to know you are", a ,"years of age",n)
x = input()
print("\nDo you want to know the time right now?")
if input() == "yes":
     import time
     now = time.ctime()
     print(now)
     y = input()
     print("\ndo you want to end chat?")
     if input() == "yes":
          print("\nCHAT ENDED")

else:
     print("\ndo you want to end chat?")
     if input() == "yes":
          print("\nCHAT ENDED")
     