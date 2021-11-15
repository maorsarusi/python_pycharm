__author__ = "Maor"


def factorial(fact):
    """
    function for calculate factorial
    :param fact: the number for the factorial
    :return: the fact!
    """
    num = 1
    for i in range(1, fact + 1):
        num *= i
    return num


def beep(string):
    """
    function to add beep to string
    :param string: the string that ew add to it beep
    :return: string + "beep"
    """
    return string + " beep"


def multiple(a, b):
    """
    function multiple multiple between 2 numbers but not if
    one of them is less than 0
    :param a: the first argument
    :param b: the second argument
    :return: the multiple between the numbers or 0 if one of them is 0
    """
    if a < 0 and b > 0:
        return "you put the number {} than the result is 0".format(a)
    elif b < 0 and a > 0:
        return "you put the number {} than the result is 0".format(b)
    else:
        return a * b


def efes(l):
    """
    function efes gets list and change it to list of zeros
    without change it id
    :param l: the list we get
    :return: the list l with zeros instead of the vars
    """
    for i in range(len(l)):
        l[i] = 0
    return l


def max_min(l):
    """
     function max_min gets a list and returns the number that appears the most time
    :param l: the list we got
    :return: the number that appears the most time
    """
    if max(l) > len(l):
        counter = [0] * max(l)
    else:
        counter = [0] * len(l)
    for i in l:
        counter[i] += 1
    return counter.index(max(counter))


def fifteen(l):
    """
    function fifteen gets a list and checks if the are to numbers with sum of 15
    :param l: the list we got
    :return: True if there are 2 numbers with sum 15
             and False if there aren't
    """
    for i in l:
        if 15 - i in l:
            return True
    return False


def Median(l):
    """
    function Median gets a list and returns the median number
    :param l: the list we got
    :return: the median number in the list
    """
    l.sort()
    return l[l.index(len(l) // 2) + 1]


def isPalindrome(l):
    """
    function isPalindrome gets a list and checks if it a palindrome
    :param l: the list we check
    :return: True if the list is a palindrome
             and False if it not
    """
    for i in range(len(l) // 2):
        if l[i] != l[len(l) - i - 1]:
            return False
    return True


def pythagoras(a, b):
    """
    function pythagoras gets to numbers represents length of sides of triangle
    and returns the third side by the formula a^2 + b^2 = c^2
    :param a: the first side of the triangle
    :param b: the second side of the triangle
    :return: the third side of the triangle
             or None if  one of the numbers are lees than 1

    """
    if a < 1:
        print("the number %s is less than 1" % repr(a))
        return None
    elif b < 1:
        print("the number %s is less than 1" % repr(b))
        return None
    else:
        c = a ** 2 + b ** 2
        print("the third side of the triangle is: ")
        return c ** 0.5


def main():
    print("%s! is : %s" % (5, factorial(5)))

    print(beep("my name is Maor Sarusi"))

    print("%s * %s = %s" % (repr(4), repr(5), multiple(4, 5)))
    print("%s * %s = %s" % (repr(-4), repr(-5), multiple(-4, -5)))
    print(multiple(-7, 8))
    print(multiple(7, -8))
    print("%s * %s = %s" % (repr(0), repr(5), multiple(0, 5)))
    l = [1, 2, 3, 4]
    l1 = efes(l)
    if id(l) == id(l1):
        print("the id's are equals and it is: " + str(id(l)))
    print("the number that appears the most times in the list is: " +
          str(max_min([1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9])))
    l = [1, 2, 3, 4, 5, 6, 8, 15, 16]
    print(" in the list %s there are two numbers that equals 15? %s" % (l, fifteen(l)))
    l = [1, 2, 3, 4, 5, 6, 8, 9, 16]
    print(" in the list %s there are two numbers that equals 15? %s" % (l, fifteen(l)))
    l = [3, 8, 4, 5, 9, 2, 1, 11]
    print("the median of the list %s is: %s" % (repr(l), repr(Median(l))))
    l = [1, 2, 3, 2, 1]
    print("the list %s is Palindrome? %s" % (repr(l), repr(isPalindrome(l))))
    l = [1, 2, 3, 4, 5, 6, 7]
    print("the list %s is Palindrome? %s" % (repr(l), repr(isPalindrome(l))))
    print(pythagoras(3, -4))
    print(pythagoras(-3, 4))
    print(pythagoras(3, 4))


if __name__ == '__main__':
    main()
