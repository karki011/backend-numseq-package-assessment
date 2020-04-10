__author__ = """
https://stackoverflow.com/questions/2068372/
fastest-way-to-list-all-primes-below-n""
"""


def primes(n):
    """ primes(n): Returns a list of all prime numbers less than n """
    numbers = set(range(n, 1, -1))
    primes_list = []
    while numbers:
        p = numbers.pop()
        primes_list.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes_list


def is_prime(m):
    """ is_prime(m) : Returns a boolean indicating
    whether m is a prime number """
    if m < 2:
        return False
    elif m == 2:
        return True
    for n in range(2, m):
        if m % n == 0:
            return False
    return True
