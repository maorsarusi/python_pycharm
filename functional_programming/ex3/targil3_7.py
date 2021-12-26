from functional_programming.ex3.tailrecurse import *


#
def napa(N):
    """
    a none tail recursion to get all prime numbers from 1 to N
    :param N:the limit to check the prime numbers
    :return:a list of all prime numbers from 1 to N
    """
    prime = [True] * N
    prime[0] = False
    # make prime to be an array of True values for prime numbers
    for i in range(2, N):
        if prime[i]:
            for mlt in range(i * 2, N, i):
                prime[mlt] = False
    res = []
    for i, item in enumerate(prime):
        if item:
            res.append(i)
    return res


#
def isPrime(n, i=2):
    """
    a function to check if a number is a prime number
    :param n: the number we check
    :param i: like a loop to check if the number has been dividend
    :return: True if the number is prime number and False if didn't
    """
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True

        # Check for next divisor
    return isPrime(n, i + 1)


#
def LOfTwins(l):
    if len(l) == 1:
        return [l[0] + 2]
    else:
        if isPrime(l[-1] + 2):

            return LOfTwins(l[:-1]) + [l[-1] + 2]
        else:
            return LOfTwins(l[:-1])


#
def reversingL(l):
    """
    a none tail recursion function to reverse a list
    :param l: the list to reverse
    :return: the reversed list
    """
    if not l:
        return []
    if len(l) == 1:
        return l
    return reversingL(l[:-1]) + [l[-1]]


#

def filteringNapa(l):
    """
    a function to filter the list we get from napa f
    :param l:
    :return: the ist after filtering
    """
    if len(l) == 1:
        return [l[0]]
    if isPrime(l[-1] + 2):

        return filteringNapa(l[:-1]) + [l[-1]]
    else:
        return filteringNapa(l[:-1])


#
def dicCreate(dic, l1, l2):
    """
    a function to create a dictionary from former dictionary
    and a key list and a value list
    :param dic: the exist dictionary
    :param l1: the keys list
    :param l2: the values list
    :return:  the container dictionary
    """
    if len(l1) == 1:
        dic[l1[0]] = l2[0]
        return dic
    else:
        dic[l1[0]] = l2[0]
        return dicCreate(dic, l1[1:], l2[1:])


# none tail recursion
def twinP(n):
    """
    a function to find twins for prime numbers
    :param n: the number we check
    :return:a dictionary with a twins prime numbers
    """
    filNapa = reversingL(filteringNapa(napa(n)))
    twins = reversingL(LOfTwins(napa(n)))
    return dicCreate({}, filNapa, twins)


#
def printingD(dictionary):
    """
    a function to print a dictionary
    :param dictionary: the dictionary to print
    """
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    printing(keys, values)


#
def printing(l1, l2):
    """
    a function to print 2 dictionary
    :param l1: the first list
    :param l2:  the second list
    """
    if len(l1) == 0:
        return
    print("the prime is:", l1[0], "and the twin is:", l2[0])
    return printing(l1[1:], l2[1:])


# tail recursion
# the same function just tail recursion

@tail_call_optimized
def filteringNapaTail(l, result):
    if len(l) == 0:
        return result
    if isPrime(l[-1] + 2):
        result += [l[-1]]
    return filteringNapaTail(l[:-1], result)


def LOfTwinsTail(l, result):
    if len(l) == 0:
        return result
    else:
        if isPrime(l[-1] + 2):
            result += [l[-1] + 2]
        return LOfTwinsTail(l[:-1], result)


#
def reversingLTail(l, result):
    if l == []:
        return result
    return reversingLTail(l[:-1], result + [l[-1]])


#
def twinPTail(n, result):
    filNapa = reversingLTail(filteringNapaTail(napa(n), []), result)
    twins = reversingLTail(LOfTwinsTail(napa(n), []), result)
    dic = {}
    return dicCreateTail(dic, filNapa, twins, dic)


#
def dicCreateTail(dic, l1, l2, result):
    if len(l1) == 0:
        return result
    else:
        result[l1[0]] = l2[0]
        return dicCreateTail(dic, l1[1:], l2[1:], result)


#
def program7():
    print(twinP(7))
    x = eval(input("enter number\n"))
    print("the values by none tail recursion is:")
    printingD(twinP(x))
    print()
    print("the values by tail recursion is:")
    dic = twinPTail(x, [])
    printingD(dic)


if __name__ == "__main__":
    program7()
