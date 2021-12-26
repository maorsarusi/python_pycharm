from functional_programming.ex3.tailrecurse import *


# none tail recursion

def pi(n):
    """
     a none tail function to sum the calculate (-1 ** (n + 1)) / ((2 * n) - 1)
     from 1 to n
    :param n: the limit to calculate
    :return: the sum
    """
    if n == 0:
        return 0
    return pi(n - 1) + ((-1 ** (n + 1)) / ((2 * n) - 1))


# tail recursion

@tail_call_optimized
def piTail(n, result):
    """
    a tail recursion function to sum the calculate (-1 ** (n + 1)) / ((2 * n) - 1)
     from 1 to n
    :param n: the limit
    :param result: the result of the calculation
    :return: the result
    """
    if n == 0:
        return result
    return piTail(n - 1, result + (-1 ** (n + 1)) / ((2 * n) - 1))


# תכנית ראשית
def program6():
    x = eval(input("enter a number:\n"))
    print("the value of pi by none tail recursion to the number", x, "is:", pi(x))
    print("the value of pi by  tail recursion to the number", x, "is:", piTail(x, 0))


# הפעלת תכנית ראשית
if __name__ == "__main__":
    program6()
