from sympy import isprime
import sys


def calculate_formula(x, y):
    return monus(2 ** x * (2 * y + 1), 1)


def monus(x, y):
    if x - y >= 0:
        return x - y
    return 0


def reduce_list(l):
    last = 0
    for i in range(len(l)):
        if l[i] != 0:
            last = i
    new_l =  l[0:last + 1]
    prime_l = []
    for i in range(len(new_l)):
        if isprime(i):
            prime_l +=  [l[i]]
    return  prime_l



def decomposition_into_prime(number):
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
    x, count = decomposition_into_prime(108)
    print(reduce_list(x))
    print(print_number(x, count))
    print(decomposition_by_formula(50))
    print(calculate_formula(0, 25))


if __name__ == '__main__':
    main()
