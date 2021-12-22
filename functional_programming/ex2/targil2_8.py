#
def add3dicts(d1, d2, d3):
    """
    a function to connect between 3 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 2nd dictionary
    :param d3: the 3rd dictionary
    :return:   the combined dictionary
    """
    d = dictCreate(d1, d2)
    dictAll = dictCreate(d, d3)
    return dictAll


#
def mergeValue(key1, key2):
    """
    a function to merge between 2 lists without duplicates values
    :param key1: the first list
    :param key2: the second list
    :return: a tuple of the combined values
    """
    l1 = set(key1)
    l2 = set(key2)
    l1Merge = list(filter(lambda i: i in l1 and not i in l2, l1))
    l2Merge = list(filter(lambda i: i in l2 and not i in l1, l2))
    lValues = l1Merge + l2Merge
    return tuple(lValues)


#
#
def findIntersectionKeys(d1, d2):
    """
    a function to find the intersections between 2 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 3nd dictionary
    :return: a list with the intersections
    """
    s = set(d1).intersection(set(d2))
    return list(s)


#
def findNoneIntersectionKeys(d1, d2):
    """
    a function to find the none intersections between 2 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 3nd dictionary
    :return: a list with the none intersections
    """
    s1 = set(d1)
    s2 = set(d2)
    l1 = list(filter(lambda i: i in s1 and not i in s2, s1))
    l2 = list(filter(lambda i: i in s2 and not i in s1, s2))
    return (l1 + l2)


#
def returnValue(d1, d2, i, l):
    """
    a function for returning value for a key from 2 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 2nd dictionary
    :param i: the index
    :param l: the list
    :return: the value from one or two dictionary
    """
    if l[i] in d1 and l[i] in d2:
        return mergeValue(d1[l[i]], d2[l[i]])
    elif l[i] in d2:
        return d2[l[i]]
    elif l[i] in d1:
        return d1[l[i]]


#
def dictCreate(d, d1):
    """
     a function to create a dictionary from 2 dictionaries to 1
    :param d:  the 1st dictionary
    :param d1: the 2nd dictionary
    :return: the merged dictionary
    """
    l = findNoneIntersectionKeys(d, d1)
    l1 = findIntersectionKeys(d, d1)
    lKeys = sorted(l1 + l)
    lValues = list(map(lambda i: returnValue(d, d1, i, lKeys), range(len(lKeys))))
    return dict(zip(lKeys, lValues))


# תוכנית ראשית
def main():
    d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
    d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
    d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])
    print("your one dictionary made by combined 3 dictionaries is: ")
    print(add3dicts(d1, d2, d3))


if __name__ == "__main__":
    main()
