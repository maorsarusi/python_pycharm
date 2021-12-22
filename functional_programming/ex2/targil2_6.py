from functional_programming.ex2 import targil2_3


# סעיף א
def pi(n):
    """
    a function to calculate a sum of a range by a formula
    :param n: the right edge of the range
    :return: the sum multiple by 4
    """
    return 4 * sum(map(lambda i: ((-1 ** (i + 1)) / ((2 * i) - 1)), range(1, n)))


# סעיף ב
def printing(x):
    """
    a function to print the value of the formula for a number to 1
    :param x: the number we starts
    """
    if x == 0:
        return
    printing(x - 1)
    print("the value is:", x, "and the value of pi is:", pi(x))


#
def checkValue():
    x = eval(input("enter an integer number" + "\n"))
    if not isinstance(x, int):
        print("must be an integer")
        checkValue()
        return
    else:
        return x


#
def program2():
    x = abs(targil2_3.checkValue())
    printing(x)


#
if __name__ == "__main__":
    program2()
