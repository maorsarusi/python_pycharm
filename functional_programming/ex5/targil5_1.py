#
def evenprt(N1, N2, N3):
    """
    a function to get the even numbers between 2 numbers
    :param N1: the 1st number
    :param N2: the 2nd number
    :param N3: the 3rd number - here for validation
    :return: a list with even number if the validation = True
    """
    if not check(N1, N2, N3):
        return []
    return [i for i in range(N1, N2 + 1) if even(i)]


def check(N1, N2, N3):
    """
    a function to check the validation of 3 numbers
    :param N1: the 1st number
    :param N2: the 2nd number
    :param N3: the 3rd number
    :return:  True if N1 < N2 and N1 < N3 < N2
              else False
    """
    if N2 < N1:
        print("N2 smaller than N1")
        return False
    elif N2 - N1 < N3:
        print("N3 must be between N1-N2")
        return False
    return True


def even(i):
    """
    a function to check if a number is even
    :param i: the number to check
    :return: True if it even
             False if it odd
    """
    return i % 2 == 0


def printing(L, N):
    """
    a function to print
    :param L: the list to print
    :param N: the length of L
    :return:
    """
    if len(L) == 0:
        return []
    print(L[0:N])
    printing(L[N:], N)


def printing1(L, N):
    [print(*L[i:N + i]) for i in range(0, len(L), N)]


def genEvenprt(N1, N2, N3):
    if not check(N1, N2, N3):
        return
    for i in range(N1, N2 + 1):
        if even(i):
            yield i


def main():
    x, y, z = eval(input("enter 3 numbers:\n"))
    print("printing by recursion:")
    printing(evenprt(x, y, z), z)
    print()
    print("printing by list comperhension:")
    printing1(evenprt(x, y, z), z)
    print("printing with generator:")
    print(printing(list(genEvenprt(x, y, z)), z))


if __name__ == "__main__":
    main()
