from sympy import isprime
import sys


def calculate_formula(x, y):
    """
    a function to calculate pair of numbers by a formula
    :param x: the left number
    :param y: the right number
    :return: the result by a formula
    """
    return monus(2 ** x * (2 * y + 1), 1)


def monus(x, y):
    """
    a function to calculate monus(minus between 2 numbers and zero if the first smaller than the second)
    :param x: the first number
    :param y: the second number
    :return:  x - y if x > y
              0     else
    """
    if x - y >= 0:
        return x - y
    return 0


def reduce_list(l):
    """
    a function to get the list of powers to the prime number
    :param l:the list of all powers
    :return:the reducing list
    """
    last = 0
    for i in range(len(l)):
        if l[i] != 0:
            last = i
    new_l = l[0:last + 1]
    prime_l = []
    for i in range(len(new_l)):
        if isprime(i):
            prime_l += [l[i]]
    return prime_l


def decomposition_into_prime(number):
    """
    a function to get the all powers for a number
    :param number: the number we gets its decomposition
    :return: a tuple of the decomposition list and counter of the decompositions

    """
    if isprime(number):
        pow_list = [0] * (number + 1)
        pow_list[number] = 1
        return pow_list, 1

    count = 0
    prime_list = [i for i in range(number) if isprime(i)]
    pow_list = [0] * (prime_list[-1] + 1)
    while True:
        for i in prime_list:
            if number % i == 0:
                if pow_list[i] == 0:
                    count += 1
                pow_list[i] += 1
                number /= i
        if number == 1:
            return pow_list, count


def print_number(l, count):
    """
    a function to print the decomposition of number by its powers
    :param l:the list of the powers
    :param count: the number of the powers that didn't 0
    :return: the decomposition of the number in the form x^y * z^w etc.
    """
    decomposition = ""
    for i in range(len(l)):
        if l[i] != 0:
            if count != 1:
                decomposition += "({}^{}) * ".format(i, l[i])
                count -= 1
            else:
                decomposition += "({}^{})".format(i, l[i])
    return decomposition


def decomposition_by_formula(number):
    """
    a function to calculate the x and y of number by the formula 2 ^ x * (2 * y + 1)
    :param number: the number we decomposing
    :return: x, y by the decomposition
    """
    number += 1
    x = 0
    y = 0
    if number % 2 != 0:
        number -= 1
    else:
        while number % 2 == 0:
            x += 1
            number //= 2
    y = number // 2
    return x, y


def main():
    x, count = decomposition_into_prime(45)
    print(reduce_list(x))
    print(print_number(x, count))
    print(decomposition_by_formula(50))
    print(calculate_formula(0, 25))


if __name__ == '__main__':
    main()
