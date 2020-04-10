def fib(n):
    """ 'n' will be the nth fibonacci number"""
    fib_tracker = {}
    retval = 0
    if n <= 2 and n >= 1:
        retval = 1
    elif n > 2:
        retval = fib(n-1) + fib(n-2)
    fib_tracker[n] = retval
    return retval
