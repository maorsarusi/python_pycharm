__author__ = "Maor"


def summer(l):
    """
    function summer gets a list and sum it
    :param l: the list we got
    :return: the summary of the list
    """
    for i in range(1, len(l)):
        l[0] += l[i]
    return l[0]


def path(p):
    """
    function path gets an address and returns the path
    :param p: the address
    :return: the path separated by space
    """
    p = p.split("/")
    string_path = ""
    for i in range(1, len(p)):
        string_path += (p[i] + " ")
    return string_path


def modulo3(a):
    """
    function modulo 3 gets number and returns the modulo 3 of the number
    :param a: the number we got
    :return: the value of modulo 3
    """
    return a % 3


def modulo3Sort(l):
    """
    the function modulo3Sort gets a list and returns it sorted by the value that
    returns from the number with modulo 3
    :param l: the list we got
    :return: the list sorted by modulo 3
    """
    l.sort(key=modulo3)
    return l


def sort2(l):
    """
    function sort2 gets a list and first sorts it by modulo 3 and after it
    sorts it from the smallest number to the biggest
    :param l: the list we got
    :return: the list sorted from the smallest number to the biggest
    """
    print("the list %s sorted by modulo 3 function from sort2 function is: %s" % (repr(l), modulo3Sort(l)))
    l.sort()
    return l


def asciiFirstAndLast(string):
    """
    the function string gets a string and returns the sum of the ascii
    of the first character and the last character in the string
    :param string: the string we got
    :return: the sum of the ascii
    of the first character and the last character in the string
    """
    return ord(string[0]) + ord(string[-1])


def asciiSort(l):
    """
    the function asciiSort gets a list and sorts it by asciiFirstAndLast function
    :param l: the list we got
    :return: the list sorts by asciiFirstAndLast
    """
    l.sort(key=asciiFirstAndLast)
    return l


""" This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Basic list exercises
Fill in the code for the functions below. main() is already set up
to call the functions with a few different inputs,
printing 'OK' when each function is correct.
The starter code for each function includes a 'return'
which is just a placeholder for your code.
It's ok if you do not complete all the functions, and there
are some additional functions to try in list2.py. """


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    sum_index = 0
    for i in words:
        if len(i) > 1:
            if i[-1] == i[0]:
                sum_index += 1
    return sum_index


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    """
    function front+x gets list of words and sort them,
    but first the words that starts with x and than in lexicographic order
    :param words: the list ew got
    :return: a sorted list
    """
    lx = []
    newWords = []
    for i in range(len(words)):
        if words[i][0] == 'x':
            lx += [words[i]]
        else:
            newWords += [words[i]]
    newWords.sort()
    lx.sort()
    return lx + newWords


def lastElement(tup):
    """
    function lastElement is helper function
    to sort_last function
    :param tup: the tuple we got
    :return: the last element in the tuple
    """
    return tup[-1]


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    """
    function sort_last gets list of tuples amd sort them
    by the last element
    :param tuples: the list we got
    :return: a sorted list by the last element in the tuples
    """
    tuples.sort(key=lastElement)
    return tuples


# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    """
    function remove_adjacent gets a list of numbers and remove
    the doubles in straight
    :param nums: thee list we got
    :return: list without doubles
    """
    if not nums:
        return []
    else:
        new_list = []
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                new_list.append(nums[i])
        new_list.append(nums[-1])
        return new_list


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#
# NOTE - DO NOT use return sorted(sorted1 + sorted2) - that's too easy :-)
#
def linear_merge(sorted1, sorted2):
    """
    function linear_merge gets two lists and merge them with sort
    :param sorted1: the first list
    :param sorted2: the second list
    :return: new list sorted. made of the two lists we got
    """
    index1 = 0
    index2 = 0
    sortList = []
    for i in range(len(sorted1) + len(sorted2)):
        if sorted1[index1] < sorted2[index2]:
            sortList += [sorted1[index1]]
            index1 += 1
        else:
            sortList += [sorted2[index2]]
            index2 += 1
        if index1 == len(sorted1):
            sortList += sorted2[index2:]
            break
        if index2 == len(sorted2):
            sortList += sorted1[index1:]
            break
    return sortList


def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """

    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print(summer([10, 11, 12, 0.75]))
    print(summer([True, False, True, True]))
    print(summer(['aa', 'bb', 'cc']))
    print(summer([[1, 2, 3, 'a'], [4, 'b', 'c', 'd']]))
    path1 = "cyber.org.il/networks/class/ex1"
    print("the path of %s is: %s " % (repr(path1), repr(path(path1))))
    l = [2, 3, 6, 7, 1, 5]
    print("the list %s sorted by modulo 3 function is: %s" % (repr(l), modulo3Sort(l)))
    l = [2, 3, 6, 7, 1, 5]
    print("the list %s sorted from the smallest to the biggest number function is: %s" % (repr(l), sort2(l)))
    l = ["aaa", "bbb", "ad", "ab"]
    print("the list %s sorted by the ascii of the first and the last character is: %s" % (repr(l), asciiSort(l)))

    print('\nmatch_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('\nfront_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print('\nsort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    print('\nremove_adjacent')
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([1, 3, 3, 2, 2, 3]), [1, 3, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print('\nlinear_merge')
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
