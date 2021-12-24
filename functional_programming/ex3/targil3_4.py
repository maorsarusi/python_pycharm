from functional_programming.ex3.tailrecurse import *
from functional_programming.ex3.targil3_3 import tailReverseNumStr


# none tail recursion
def isPalindrome(n):
    """
    a function to check if a number is a palindrome by none tail recursion
    :param n: the number we checks
    :return: True if the number is a palindrome and False if it didn't
    """
    strN = str(n)
    if len(strN) == 0:
        return True
    if len(strN) == 1:
        return True
    if not strN[0] == strN[-1]:
        return False
    return isPalindrome(int(strN[1:-1]))


# tail recursion str

@tail_call_optimized
def reversing(n, result):
    """
    a function to reverse a number
    :param n: the original number
    :param result: the reversed number
    :return: result
    """
    if isinstance(n, int):
        if n < 0:
            n *= -1
    strN = str(n)
    if strN == "":
        return result
    return tailReverseNumStr(strN[:-1], result + strN[-1])


def tailiIsPalindrome(n, result):
    """
    a tail recursion function to check if number is a palindrome
    :param n: the original number
    :param result: the result of the reverse
    :return: True if the number is a palindrome
             and False if it didn't
    """
    x = reversing(n, result)
    if x == str(n):
        return True
    else:
        return False


# תכנית ראשית
def program4():
    x = eval(input("enter the number you want to check\n"))
    string = ""
    y = isPalindrome(x)
    z = tailiIsPalindrome(x, "")
    if y is False and z is False:
        string = "it isn't a palindrome"
    else:
        string = "it's a palindrome"
    print("isPalindrome by none tail recursion on the number", x, "says that", string)
    print("isPalindrome by  tail recursion on the number", x, "says that", string)


# הפעלת תכנית ראשית
if __name__ == "__main__":
    program4()
