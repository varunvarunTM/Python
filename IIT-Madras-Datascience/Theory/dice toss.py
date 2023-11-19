import random
x = random.randrange(1,7)
choice = input("Do you want an infinite dice toss? : Type yes or no\n")
if choice == "yes":
    while True:
        x = random.randrange(1,7)
        print(x)
else:
    print(x)

