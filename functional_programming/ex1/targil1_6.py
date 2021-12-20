def sortInDictionary(L):
    """
    a function that gets a list and return a dictionary ordered by types that counting all types in the list
    :param L: our list
    :return:the dictionary we got
    """
    dic = dict.fromkeys({'list', 'int', 'float', 'str', 'tuple'})
    count = 0
    for i in range(len(L)):
        string = str(type(L[i]))
        string1 = string[8:len(string) - 2]
        if dic[string1] is None:
            count = 0
        else:
            count = dic[string1]
        dic[string1] = count + 1
    return dic


# תוכנית ראשית
def main():
    L = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']
    x = sortInDictionary(L)
    for keys, values in x.items():
        if values is None:
            print(keys + ":", 0)
        else:
            print(keys + ":", values)


if __name__ == '__main__':
    main()
