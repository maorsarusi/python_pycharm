def check(x):
    """
    a function to check the type of a parameter
    :param x: the parameter
    :return:  true if it a number anf false if it didn't
    """
    if type(x) is int or type(x) is float or type(x) is complex:
        return True
    else:
        return False


def middle(x, y, z, w):
    """
    a function to return the 2 middle numbers from 4
    :param x: the 1st number
    :param y: the 2nd number
    :param z: the 3rd number
    :param w: the 4th number
    :return:  the 2 middle numbers by size
    """
    L = [x, y, z, w]
    for i in range(len(L) - 1, 0, -1):
        for j in range(i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    result = L[1], L[2]
    return result


def middleSort(x, y, z, w):
    """
     another function to return the 2 middle numbers from 4
    :param x: the 1st number
    :param y: the 2nd number
    :param z: the 3rd number
    :param w: the 4th number
    :return:  the 2 middle numbers by size
    """
    l = [x, y, z, w]
    l.sort()
    result = l[1], l[2]
    return result


def checkTuple(x):
    """
    a function that gets a tuple and return which value isn't a number
    :param x: the tuple we got
    :return:  true if the term is a number and false if it didn't
    """
    print("the values of the tuple are: ")
    print(x)
    print("---------------")
    for i in x:
        if not type(i) is int and not type(i) is float and not type(i) is complex:
            print("the value: '" + i + "' isn't a number")
            print("---------")
            return False
    return True


def middleTuple(x):
    """
    a function that get a tuple and returns the middle values in it
    :param x: our tuple
    :return: the middle values in x
    """
    tmp = sorted(x)
    print("the values after sorting: ")
    print(tmp)
    y = len(tmp)
    if y % 2 == 0:
        print("the two middle numbers at 'w' are: ")
        result = tmp[(int)(y / 2) - 1], tmp[(int)(y / 2)]
    return result


# תוכנית ראשית

def main():
    a = eval(input("Enter a value for a: "))
    print("the value for a is: ")
    print(check(a))
    b = eval(input("Enter b value for a: "))
    print("the value for b is: ")
    print(check(b))
    c = eval(input("Enter a value for a: "))
    print("the value for c is: ")
    print(check(c))
    d = eval(input("Enter a value for d: "))
    print("the value for d is: ")
    print(check(d))
    print("--------")
    print("middle")
    print(middle(a, b, c, d))
    print("--------")
    print("middleSort")
    print(middleSort(a, b, c, d))
    print("==============")
    z = tuple([5, "a", 4])
    t = checkTuple(z)
    w = (100, 20, 35, 40, 67, 32)
    if checkTuple(w) == True:
        print("all values are good")
        print("------------")
        print(middleTuple(w))


if __name__ == '__main__':
    main()