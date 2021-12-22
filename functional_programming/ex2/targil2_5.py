#
from functools import reduce


# סעיף א
def m1(n):
    """
    a function to calculate a sum of the numbers by the formula x / (x +1) from 1 to x +1
    :param n: the edge of the range
    :return: the sum
    """
    return sum(map(lambda i: i / (i + 1), range(1, n + 1)))


#
def m2(n):
    return reduce(lambda x, y: x + y, map(lambda i: i / (i + 1), range(1, n + 1)))


# סעיף ב
def checkValue():
    """
    a function to check a validation of a number
    :return: the number after validation
    """
    x = eval(input("enter an integer number" + "\n"))
    if isinstance(x, int) or x < 1:
        return x
    else:
        print("must be an integer")
        return checkValue()


#
def printing(i):
    """
    a function to print the calculation
    :param i: the number that helps to calculate
    """
    if i == 0:
        return
    printing(i - 1)
    print("the values is:", i, ",and the value of sum till this num  is:", m1(i))


#
def program1():
    x = abs(checkValue())
    printing(x)


# תוכנית ראשית
if __name__ == "__main__":
    program1()
