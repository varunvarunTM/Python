import random
x = random.random()
choice = input("Do you want an infinite coin toss? : Type yes or no\n")
if choice == "yes":
    while x != 0.5:
        x = random.random()
        print("heads") if x > 0.5 else print("tails")
        if x == 0.5:
            print("edge")
            break
else:
    print("heads") if x > 0.5 else print("tails")
    if x == 0.5:
            print("edge")

