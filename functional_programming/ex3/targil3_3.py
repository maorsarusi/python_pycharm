from functional_programming.ex3.tailrecurse import *


# none tail recursion str
def reverseNumStr(n):
    """
    a function to reverse a number (string, none tail recursion)
    :param n: the number to reverse
    :return: the reversed number (string)
    """
    if isinstance(n, int):
        if n < 0:
            n *= -1
    strN = str(n)
    if strN == "":
        return ""
    return reverseNumStr(strN[1:]) + (strN[0])


# none tail recursion list

def reverseNumLst(n):
    """
    a function to reverse a number (list, none tail recursion)
    :param n: the number to reverse
    :return: the reversed number (list)
    """
    if isinstance(n, int):
        if n < 0:
            n *= -1
    if not isinstance(n, list):
        lstN = list(str(n))
    else:
        lstN = n
    if not lstN:
        return []
    return reverseNumLst(lstN[1:]) + [lstN[0]]


# tail recursion str

@tail_call_optimized
def tailReverseNumStr(n, result):
    """
    a function to reverse a number (string, tail recursion)
    :param n: the number to reverse
      :param result: the result of the number
    :return: the reversed number (string)
    """
    if isinstance(n, int):
        if n < 0:
            n *= -1
    strN = str(n)
    if strN == "":
        return result
    return tailReverseNumStr(strN[:-1], result + strN[-1])


# tail recursion list

def tailReverseNumLst(n, result):
    """
    a function to reverse a number (list, tail recursion)
    :param n: the number to reverse
    :param result: the result of the list
    :return: the reversed number (list)
    """
    if isinstance(n, int):
        if n < 0:
            n *= -1
    if not isinstance(n, list):
        lstN = list(str(n))
    else:
        lstN = n
    if not lstN:
        return result
    return tailReverseNumLst(lstN[:-1], result + [lstN[-1]])


def checkValue():
    x = int(input("Enter an integer number" + "\n"))
    if not type(x) == type(1):
        print("must be an integer" + "\n")
    else:
        return x


# תוכנית ראשית
def program3():
    x = checkValue()
    print("the reversed of num:", x, "by none tail recursion str is:", reverseNumStr(x))
    print("the reversed of num:", x, "by  tail recursion str is:", tailReverseNumStr(x, ""))
    print("the reversed of num:", x, "by  tail recursion list is:", reverseNumLst(x))
    print("the reversed of num:", x, "by  tail recursion list is:", tailReverseNumLst(x, []))


if __name__ == "__main__":
    program3()
