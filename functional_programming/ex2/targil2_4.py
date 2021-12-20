from functional_programming.ex2 import targil2_3


#
def isPalindrome(n):
    """
    a function to check if a number is a palindrome
    :param n: the number
    :return: true if ir a palindrome and false if it didn't
    """
    return n == targil2_3.reverseNum1(n)


#
def myPrt(isPal):
    """
    a function to organize the decision if it palindrome or not
    :param isPal: the number we check
    """
    if isPal:
        print("it is a palindrome")
    else:
        print("it isn't a palindrome")
    return


#
def program():
        n = targil2_3.checkValue()
        if n > 0:
            myPrt(isPalindrome(n))

        elif n < 0:
            myPrt(isPalindrome(n * -1))
        else:
            print("the input must be an integer")


# הרצה של התרגיל שנוכל להשתמש בו כמודול
if __name__ == "__main__":
    program()
