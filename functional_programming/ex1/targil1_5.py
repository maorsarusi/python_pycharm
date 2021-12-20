def listOfTuples(x):
    """
    a function that gets a list and return a list with all tuples in it
    :param x: the bigger list
    :return: sub list with the tuples in the bigger list
    """
    length = len(x)
    i = 0
    L = []
    while i < length:
        if isinstance(x[i], tuple):
            L.append(x[i])
        i = i + 1
    return L


def tupleOfLists(x):
    """
    a function that gets a list and return a tuple with all lists in it
    :param x: the bigger list
    :return: a tuple with all the lists in the bigger lists
    """
    length = len(x)
    i = 0
    L = []
    while i < length:
        if isinstance(x[i], list):
            L.append(x[i])
        i = i + 1
    M = tuple(L)
    return M


def listOfStrings(x):
    """
    a function that gets a list and return a list with all strings in it
    :param x: the bigger list
    :return: sub list with the strings in the bigger list
    """
    length = len(x)
    i = 0
    L = []
    while i < length:
        if isinstance(x[i], str):
            L.append(x[i])
        i = i + 1
    return L


def ListOfNumbs(x):
    """
    a function that gets a list and return a list with all numbers in it
    :param x: the bigger list
    :return: sub list with the numbers in the bigger list
    """
    length = len(x)
    i = 0
    L = []
    while i < length:
        if isinstance(x[i], int) or isinstance(x[i], float) or isinstance(x[i], complex):
            L.append(x[i])
        i = i + 1
    return L


# תוכנית ראשית
def main():
    L = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']
    print("list of tuples are:")
    print(listOfTuples(L))
    print("tuples of list are:")
    print(tupleOfLists(L))
    print("list of strings are:")
    print(listOfStrings(L))
    print("List of numbers are:")
    print(ListOfNumbs(L))


if __name__ == '__main__':
    main()
