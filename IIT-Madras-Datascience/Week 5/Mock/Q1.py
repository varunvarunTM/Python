""" Write a recursive function named fibo that accepts a positive
    integer n as argument and returns the n th Fibonacci number.
    For this problem, F(1) = F(2) = 1 are the first two Fibonacci numbers.

    You do not have to accept input from the user or print output to the
    console. You just have to write the function definition. """



def fibo(n):
    """
    compute the nth fibonacci integer
	
    Argument:
        n: int
    Return:
        f_n: int
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)