def sumDigits1(n):
    """
    function to calculate sum of digits of a number
    :param n: the number
    :return: the sum of the digits
    """
    return sum(perukN1(n))


# זה הולך ההבדל זה לאיזה גירסא של פירוק
def sumDigits2(n):
    return sum(perukN2(n))


# reversed  גירסא לא מדוייקת
def perukN1(n):
    """
    a function to decomposition a number
    :param n: the number
    :return: the decomposition of the number
    """
    Lout = []
    while n > 10:
        n, firstDigit = perukStep(n)
        Lout.append(firstDigit)
    else:
        Lout.append(n)
    return list(reversed(Lout))


#
def perukStep(n):
    """
    a function to get a number and decomposing it to digits
    :param n: the number
    :return: a tuple with the units and tenth digits
    """
    return n // 10, n % 10


# גירסא לא מדוייקת insert
def perukN2(n):
    Lout = []
    while n > 10:
        n, firstDigit = perukStep(n)
        Lout.insert(0, firstDigit)
    else:
        Lout.insert(0, n)
    return Lout


# סעיף ב
def sumDigits3(n):
    return sum(map(int, list(str(abs(n)))))


# תכנית ראשית
if __name__ == "__main__":
    while True:
        try:
            a = int(input("enter a number positive or negative" + "\n"))
        except ValueError:
            print("must be an integer")
            continue
        else:
            print("sumDigits1: " + str(sumDigits1(a)) + " and sumDigits3: " + str(sumDigits3(a)))
        break
