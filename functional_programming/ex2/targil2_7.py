#
# eratosthenes.py
# The Eratosthenes' algorithm
#
from functools import reduce


def napa(N):
    """
    an algorithm to calculate all prime number till a number
    :param N: the limit
    :return: a list with all the prime numbers
    """
    prime = [True] * N
    prime[0] = False
    # make prime to be an array of True values for prime numbers
    for i in range(2, N):
        if prime[i]:
            for mlt in range(i * 2, N, i):
                prime[mlt] = False
    res = []
    for i, item in enumerate(prime):
        if item:
            res.append(i)
    return res


#
def isPrime(n):
    """
    a function to check if a number is a prime number
    :param n: the number to check
    :return: True if it a prime and False if didn't
    """
    if n == 1:
        return True
    elif n == 0:
        return False
    return not any(map(lambda i: n % i == 0, range(2, n)))


#
def napaFiltering(n):
    """
    a function to filter a primes number by a condition
    :param n: the number we get till it the prime numbers
    :return: a list by the condition(if the number + 2 is prime )
    """
    return list(filter(lambda i: isPrime(i + 2), napa(n)))


#
def napaFilterinPlus2(n):
    return list(map(lambda i: napaFiltering(n)[i] + 2, range(len((napaFiltering(n))))))


# סעיף א
def twinp(n):
    return dict(zip(napaFiltering(n), napaFilterinPlus2(n)))


def Printing(d, length):
    """
    a function to print a prime number and its twin
    :param d: our prime list
    :param length: the length of the list
    """
    if length == 0:
        return
    Printing(d, length - 1)
    print("the prime is: " + str(list(d.keys())[length - 1]) + " and the twin is: " + str(list(d.values())[length - 1]))


#
def program3():
    x = eval(input("enter a value\n"))
    print(napaFiltering(x))
    Printing(twinp(x), len(twinp(x)))


# תוכנית ראשית
if __name__ == "__main__":
    program3()
