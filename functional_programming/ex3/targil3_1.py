from functional_programming.ex3.tailrecurse import *


def pentaNumRangeNone(n1, n2):
    """
    a function to calculate a number by a formula with limits
    :param n1: the left limit
    :param n2: the right limit
    :return: a list the penta numbers by the limits
    """
    getPentaNum = lambda i: i * (3 * i - 1) / 2
    return pentaLst(getPentaNum, n1, n2)


# non tail recursion
def pentaLst(getPentaNum, n1, n2):
    """
    a function to get a list by none tail recursion of the penta numbers by thr limits
    :param getPentaNum: a function to calculate the penta numbers
    :param n1: the left limit
    :param n2: the right limit
    :return: the penta list
    """
    if n1 == n2:
        return []
    else:
        return [getPentaNum(n1)] + pentaLst(getPentaNum, n1 + 1, n2)

    # tail recursion


@tail_call_optimized
#
def pentaNumRangetail(n1, n2):
    getPentaNum = lambda i: i * (3 * i - 1) / 2
    return tailPentaLst(getPentaNum, n1, n2, [])


def tailPentaLst(getPentaNum, n1, n2, result):
    """
    a function to get a list by  tail recursion of the penta numbers by thr limits
    :param getPentaNum: a function to calculate the penta numbers
    :param n1: the left limit
    :param n2: the right limit
    :return: the penta list
    """
    if (n1 == n2):
        return result
    else:
        return tailPentaLst(getPentaNum, n1 + 1, n2, result + [getPentaNum(n1)])


#
def get2Nums():
    """
    a function to get 2 numbers from the user
    :return: the numbers if the first is smaller than the second
             and False if didn't
    """
    n1 = int(input("enter the value of  n1:"))
    n2 = int(input("enter the value of  n2 it must be bigger than n1:"))
    if isinstance(n1, int) and n1 > 0 and isinstance(n2, int) and n1 < n2:
        return n1, n2
    return False


# תכנית ראשית
def program1():
    n1, n2 = get2Nums()
    print("none tail: ", pentaNumRangeNone(n1, n2))
    print("     tail: ", pentaNumRangetail(n1, n2))


# הפעלת תכנית ראשית
if __name__ == "__main__":
    program1()
