from functional_programming.ex3.tailrecurse import *


#
def getKeys(d1):
    """
   a function to get keys' dictionary
   :param d1: the dictionary
   :return: a list with all keys
   """
    return list(d1.keys())


#
def sameKeys(l1, l2):
    """
   a function to print the keys that the same between 2 lists
   :param l1: the 1st list
   :param l2: the 2nd list
   :return: a list with the same keys
   """
    if len(l1) == 0:
        return []
    if l1[-1] in l2:
        return sameKeys(l1[:-1], l2) + [l1[-1]]
    else:
        return sameKeys(l1[:-1], l2)


#
def difKeys(l1, l2):
    """
    a function to get the keys that is different between 2 lists
    :param l1: the 1st list
    :param l2: the 2nd list
    :return: a list with the different keys
    """
    if len(l1) == 0:
        return []
    if l1[-1] in l2:
        return difKeys(l1[:-1], l2)
    else:
        return difKeys(l1[:-1], l2) + [l1[-1]]


#
def mergeSame(l, d1, d2):
    """
    a function to merge the values in same keys in 2 dictionaries
    :param l: the keys that same in thw 2 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 2nd dictionary
    :return: a list with tuples with the values that merged
    """
    if len(l) == 0:
        return []
    value = d1[l[-1]], d2[l[-1]]
    return mergeSame(l[:-1], d1, d2) + [value]


#
def enterSame(l, l1):
    """
    a function to enter the same keys in 2 lists
    :param l: the 1st list
    :param l1: the 2nd lst
    :return: a list with the same keys
    """
    if len(l) == 0:
        return []
    return enterSame(l[:-1], l1[:-1]) + [(l[-1], l1[-1])]


#
def mergeDif(l, d1, d2):
    """
    a function to merge the values of 2 dictionaries with the different keys
    :param l: the different keys
    :param d1: the 1st dictionary
    :param d2: the 2nd dictionary
    :return: a list of with the keys and their values
    """
    if len(l) == 0:
        return []
    d1Keys = getKeys(d1)
    if l[-1] in d1Keys:
        return mergeDif(l[:-1], d1, d2) + [(l[-1], d1[l[-1]])]
    else:
        return mergeDif(l[:-1], d1, d2) + [(l[-1], d2[l[-1]])]


def enterKeys(d1, d2):
    """
    a function to combine between 2 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 2nd dictionary
    :return: the combined dictionary
    """
    d1K = getKeys(d1)
    d2K = getKeys(d2)
    same = sameKeys(d1K, d2K)
    dif = difKeys(d1K, d2K) + difKeys(d2K, d1K)
    merge = mergeSame(same, d1, d2)
    l = enterSame(same, merge) + mergeDif(dif, d1, d2)
    return dict(l)


def addict(d1, d2, d3):
    """
    a function to combine between 3 dictionaries
    :param d1: the 1st dictionary
    :param d2: the 2nd dictionary
    :param d3: the 3rd dictionary
    :return: the combined dictionary
    """
    d = enterKeys(d1, d2)
    d4 = enterKeys(d, d3)
    return d4


@tail_call_optimized
# tail recursion
# the same functions just in tail recursion
def sameKeysTail(l1, l2, result):
    if len(l1) == 0:
        return result
    if l1[0] in l2:
        return sameKeysTail(l1[1:], l2, result + [l1[0]])
    return sameKeysTail(l1[1:], l2, result)


#
def difKeysTail(l1, l2, result):
    if len(l1) == 0:
        return result
    if not l1[0] in l2:
        return difKeysTail(l1[1:], l2, result + [l1[0]])
    return difKeysTail(l1[1:], l2, result)


#
def enterKeysTail(d1, d2):
    d1K = getKeys(d1)
    d2K = getKeys(d2)
    same = sameKeysTail(d1K, d2K, [])
    dif = difKeysTail(d1K, d2K, []) + difKeysTail(d2K, d1K, [])
    merge = mergeSameTail(same, d1, d2, [])
    l = enterSameTail(same, merge, []) + mergeDifTail(dif, d1, d2, [])
    return dict(l)


#
def mergeSameTail(l, d1, d2, result):
    if len(l) == 0:
        return result
    value = d1[l[-1]], d2[l[-1]]
    return mergeSameTail(l[:-1], d1, d2, [value] + result)


#
def enterSameTail(l1, l2, result):
    if len(l1) == 0:
        return result
    return enterSameTail(l1[:-1], l2[:-1], [(l1[-1], l2[-1])] + result)


#
def mergeDifTail(l, d1, d2, result):
    if len(l) == 0:
        return result
    d1Keys = getKeys(d1)
    d2Keys = getKeys(d2)
    if l[-1] in d1Keys:
        return mergeDifTail(l[:-1], d1, d2, [(l[-1], d1[l[-1]])] + result)
    else:
        return mergeDifTail(l[:-1], d1, d2, [(l[-1], d2[l[-1]])] + result)


#
def addictTail(d1, d2, d3):
    d = enterKeysTail(d1, d2)
    dAll = enterKeysTail(d, d3)
    return dAll


# תכנית ראשית
def program8():
    d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
    d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
    d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])
    print("the union dictionary by none tail recursion is:")
    print(addict(d1, d2, d3))
    print("the union dictionary by  tail recursion is:")
    print(addictTail(d1, d2, d3))


# הפעלת תכנית ראשית
if __name__ == "__main__":
    program8()
