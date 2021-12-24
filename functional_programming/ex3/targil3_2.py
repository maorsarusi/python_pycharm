# סעיף א
# non tail recursion
def sumDigit1(n):
    """
    a function to calculate the digits of a number
    :param n: the number
    :return:  the sum of its digits
    """
    return mySum1(createLst1(n))


#
def mySum1(L):
    """
    a function to calculate sum of numbers in list by none tail recursion
    :param L: the list we got
    :return:  the sum of the list
    """
    if not L:
        return 0
    return mySum1(L[1:]) + L[0]


#
def createLst1(n):
    """
    a function that get a number and creates a list from its digits
    :param n: the number
    :return: a list from the digits of the number
    """
    if n // 10 == 0:
        return [n]
    else:
        return createLst1(n // 10) + [n % 10]


# tail recursion

def mySum2(L, result):
    if not L:
        return result
    return mySum2(L[1:], result + L[0])


#
def createLst2(n):
    """
    a function that get a number and creates a list from its digits
    :param n: the number
    :return: a list from the digits of the number
    """
    if n // 10 == 0:
        return [n]
    return createLst2(n // 10) + [n % 10]


# סעיף ב
def createLst3(n):
    """
    a function that get a number and creates a list from its digits
    :param n: the number
    :return: a list from the digits of the number
    """
    if n == "":
        return 0
    else:
        return createLst3(n[1:]) + n[0]


#
def sumDigit3(n):
    return mySum2(createLst2(n), 0)


# תכנית ראשית
def program2():
    x = eval(input("enter a number" + "\n"))
    print("sum digits of the number:", x, "by none tail recursion is:", sumDigit1(x))
    print("sum digits of the number:", x, "by  tail recursion is:", sumDigit3(x))


# הפעלת תכנית ראשית
if __name__ == "__main__":
    program2()
