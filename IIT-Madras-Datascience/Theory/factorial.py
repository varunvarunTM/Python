while True:
    n = int(input())
    factorial = 1
    if n >= 1:
        while n >= 1:
            factorial = factorial * n
            n = n-1
    elif n < 0:
        factorial = "Not Defined"
    else:
        factorial = 1
    print(factorial)