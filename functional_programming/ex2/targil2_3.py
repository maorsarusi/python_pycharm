# סעיף א
def reverseNum1(n):
    """
    a function to reverse a number
    :param n: the number(integer)
    :return: the reverse number
    """
    strN = str(abs(n))
    return int(strN[::-1])


# סעיף ב
def reverseNum2(n):
    """
    a function to reverse number
    :param n: the number
    :return:  a list of reversed digits for the number
    """
    lstN = str(abs(n))
    return list(reversed(lstN))


# סעיף ג
def checkValue():
    """
    a function to check if the parameter is an integer
    :return: the number
    """
    num = input("Enter an integer number" + "\n")
    while not num.isdigit():
        if num[0] != "-":
            print("must be an integer" + "\n")
            num = input("Enter an integer number" + "\n")
    else:
            return int(num)


# תוכנית ראשית
if __name__ == "__main__":
    x = checkValue()
    print("the value by reverseNum1 is: " + str(reverseNum1(x)))
    print("the value by reverseNum2 is: " + str(reverseNum2(x)))
