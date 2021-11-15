__author__ = "Maor"


# chapter 3
def age(Age):
    """
    function that checks age
    :param Age: the age that we got
    :return:  a sentence by the age
    """
    if Age == 18:
        return "Congratulations"
    elif Age < 18:
        return "You are so young"
    else:
        return "We love old people"


# chapter 4
def inigoMontoya(string):
    """
    function for slicing a string ("Hello, my name is Inigo Montoya")
    :param string: the sentence that we slice
    :return: the sentence with slices
    """
    hello = string[0:string.index(',')]
    my_name = string[7:15]
    jumps = string[::2]
    slices = string[3:string.index(',')] + " " + string[8:14:2] + " " + string[16:19:2]
    print(hello + "\n" + my_name + "\n" + jumps + "\n" + slices + '\n')


# chapter 5

def multi(a, b):
    """
    function for multiple two numbers
    :param a: the first number
    :param b: the second number
    :return: the multiple between a and b
    """
    return a * b


def divide(a, b):
    """
    function for dividing two numbers
    :param a: the first number
    :param b: the second number can't be zero
    :return:  the division of a and b
    """
    if b == 0:
        return "illegal"
    else:
        return a / b


# chapter 6

def jump2(l):
    """
    function jump2 gets a list and returns the items in jump 2 (the items in the odd place and the items in the pair places)
    :param l: the list we got
    :return: 2 lists by odd places and pair plaes
    """
    return l[::2], l[1::2]


def main():
    Age = 18
    print(" the age is: %s %s" % (repr(Age), repr(age(Age))))

    Age = 27
    print(" the age is: %s %s" % (repr(Age), repr(age(Age))))

    Age = 12
    print(" the age is: %s %s" % (repr(Age), repr(age(Age))))

    inigoMontoya("Hello, my name is Inigo Montoya")

    print(multi(3, 6))
    print(multi(0, 8))

    print(divide(4, 2))
    print(divide(4, 5))
    print(divide(4, 0))

    print(jump2([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
