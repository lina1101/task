import math
import time


def fibonacci(n):
    """
    Calculates fibonacci sequence up until provided nth entry.
    :param n:
    :return:
    """
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


def factorial(n):
    """
    This is just a wrapper to ensure arg name compatibility with our forms, why reinvent the wheel?
    """
    return math.factorial(n)


def time_func(f, *args, **kwargs):
    """
    :param f: Input function
    :param args: args to pass to input function
    :param kwargs: kwargs to pass to input function
    :return: Execution time in ms and return from input function
    """
    start = time.time()
    ret = f(*args, **kwargs)
    end = time.time()

    return (end - start) * 1000, ret
