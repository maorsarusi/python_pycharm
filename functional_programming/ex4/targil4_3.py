def sortedZip(L):
    return list(zip(*[sorted(item) for item in L]))


#
def sortedZipreversed(L):
    return list(zip(*[reversed(item) for item in L]))


#
def funcZip(func, L):
    return list(zip(*[func(item) for item in L]))


#
def unZippy(L):
    return list(zip(*[(item) for item in L]))


def twoTimes(x):
    return [2 * item for item in x]


#
def main():
    L = [(3, 1, 2), (5, 6, 4), ('a', 'b', 'c')]
    print("sorted zip by funcZip:")
    print(funcZip(sorted, L))
    print("sorted zip by sortedZip:")
    print(sortedZip(L))
    print()
    print(" reversed zip by funcZip:")
    print(funcZip(reversed, L))
    print("reversed zip by sortedZipreversed:")
    print(sortedZipreversed(L))
    print("sorted zip by unZippy (the first argumant):")
    print(unZippy(L))

    dicOPerations = dict(zip([1, 2, 3], [sorted, reversed, twoTimes]))

    List = eval(input("input a nested list:\n"))
    if List == [] or not isinstance(List, list):
        print("you didn't choose any list so we took that one:  [(3,1,2),(5,6,4),('a','b','c')]\n")
        List = L
    operation = eval(input("input an oparetion to sort enter 1 to reversed enter 2 and to multiply by 2 enter 3:\n "))
    print(funcZip(dicOPerations[operation], List))


main()
