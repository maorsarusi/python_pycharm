# map גירסא 1 עם
import sys


def pentaNumRange1(n1, n2):
    """
    a function to calculate a range of numbers by the formula n * (3 * n - 1) / 2
    :param n1: the left edge of the range
    :param n2: the right edge of the range
    :return: a list with all the calculation
    """
    getPentaNum = lambda n: n * (3 * n - 1) / 2
    return list(map(getPentaNum, range(n1, n2)))


# גירסא 2 עם לולאות
def pentaNumRange2(n1, n2):
    getPentaNum = lambda n: n * (3 * n - 1) / 2
    lout = []
    for i in range(n1, n2):
        lout.append(getPentaNum(i))
    return lout


# גירסא 3 יותר פונקציונלי
def pentaNumRange3(n1, n2):
    lout = []
    for i in range(n1, n2):
        lout.append((lambda n: n * (3 * n - 1) / 2)(i))  # זה ההבדל מגרסא 2
    return lout


#
def prtAux(pentaNumberLst):
    for i in range(0, len(pentaNumberLst), 10):
        print(pentaNumberLst[i:i + 10])


#
def prtPentNum():
    while True:
        try:
            n1 = int(input("enter the value of  n1:"))
        except ValueError:
            print("must be an integer")
            continue
        else:
            while True:
                try:
                    n2 = int(input("enter the value of  n2 it must be bigger than n1:"))
                except ValueError:
                    print("must be an integer")
                    continue
                else:
                    if n2 < n1:
                        print("must be bigger than n1")
                    else:
                        prtAux(pentaNumRange1(n1, n2))
                    return


# ללא לולאות
def prtPentNum1():
    inValues = get2Nums()
    if not inValues:
        print("ERROR")
        sys.exit()
    n1, n2 = inValues
    pentaPrt1(pentaNumRange1(n1, n2))


#
def pentaPrt1(L):
    print(list(map(lambda i: L[i:i + 10], range(0, len(L), 10))))


#
def get2Nums():
    n1 = int(input("enter the value of  n1:"))
    n2 = int(input("enter the value of  n2 it must be bigger than n1:"))
    if isinstance(n1, int) and n1 > 0 and isinstance(n2, int) and n1 < n2:
        return n1, n2
    return False


# הפעלת תכנית ראשית

if __name__ == "__main__":
    prtPentNum1()
