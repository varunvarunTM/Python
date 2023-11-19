""" Write the following functions:

        (1) factors:
                accept a positive integer n as argument.
                Return the set of all factors of n.

        (2) common_factors: 
                accept two positive integers a and b as arguments.
                Return the set of common factors of the two numbers.
                This function must make use of factors.

        (3) factors_upto:
                accept a positive integer n as argument.
                Return a dict D, whose keys are integers and values are sets.
                Each integer in the range [1,n], endpoints inclusive,
                is a key of D. The value corresponding to a key,
                is the set of all factors of key.
                This function must make use of factors.

    The idea we are trying to bring out here is to make use of pre-defined
    functions whenever needed. """



def factors(n):
    """
    Compute the set of factors of n
			
    Argument:
        n: integer
    Return:
        factors_of_n: set
    """
    factors_set = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors_set.add(i)
            factors_set.add(n // i)
    return factors_set

def common_factors(a, b):
    """
    Compute the set of common factors of a and b

    Arguments:
        a, b: integers
    Return:
        factors_common: set
    """
    factors_a = factors(a)
    factors_b = factors(b)
    return factors_a.intersection(factors_b)


def factors_upto(n):
    """
    Get the factors up to n 
	
    Argument:
        n: integer
    Return:
        result: dict (keys: integers, values: sets)
    """
    factors_dict = {}
    for i in range(1, n + 1):
        factors_dict[i] = factors(i)
    return factors_dict