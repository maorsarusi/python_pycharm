def shiftL(binNr, N):
    """
    a function that does the operation of shift left in binary number
    :param binNr: our binary number
    :param N: how many digits we move left
    :return: the number after shift left
    """
    if N > len(binNr):
        s = "N is bigger than length"
        return s
    else:
        s = binNr[N:len(binNr)]
        s = s + "0" * N
        return s


def shiftR(binNr, N):
    """
    a function that does the operation of shift right in binary number
    :param binNr: our binary number
    :param N: how many digits we move right
    :return: the number after shift right
    """
    if N > len(binNr):
        s = "N is bigger than length"
        return s
    else:
        s = "0"
        s = s + "0" * (N - 1)
        s = s + binNr[0:len(binNr) - N]
        return s


def shiftCL(binNr, N):
    if N > len(binNr):
        s = "N is bigger than length"
        return s
    s = binNr[0:N]
    t = binNr[N:len(binNr)]
    return t + s


def shiftCR(binNr, N):
    if N > len(binNr):
        s = "N is bigger than length"
        return s
    else:
        s = binNr[len(binNr) - N:len(binNr)]
        t = binNr[0:len(binNr) - N]
        return s + t


# תוכנית ראשית
def main():
    x = "110001110"
    print(shiftL(x, 1))
    print(shiftR(x, 3))  # אני הבנתי להוריד מימין ולהוסיף לשמאל
    print(shiftCL(x, 2))
    print(shiftCR(x, 2))


if __name__ == '__main__':
    main()
