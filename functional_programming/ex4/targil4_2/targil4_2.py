# 'פונקציות לסעיף א
# method to create a dictionary from a sentence and to check if it written with no numbers
# הערה:בשביל דיוק פונקציונאלי עדיף הכל בשורה אחת

def treatLine(lineNr, line):
    """
    a function to manage the decomposition of a line in a text
    :param lineNr: a number to check if we had a number in the line
    :param line: a line from a text
    :return: a tuple with lineNr and the dictionary we creates
    """
    keys = line.split()
    vowels = listOfSentence(keys, crateListVByWord)
    tup = enterToATuple(vowels)
    consonantbm = listOfSentence(keys, createListbmByWord)
    tup += enterToATuple(consonantbm)
    consonantnz = listOfSentence(keys, createListnzByWord)
    tup += enterToATuple(consonantnz)
    values = list(zip(*[item for item in tup]))
    d = createDic(keys, values, {})
    return tuple([lineNr]) + (d,)


# method to check if it written with no numbers
def checkAllLetters(line):
    """
    a function to check if a line is with a number
    :param line:
    :return:
    """
    if not all([False for i in range(0, len(line)) for j in range(0, len(line[i])) if
                "9" >= line[i][j] >= '1']):
        return -1
    return 1


# method to create a list of vowels from a word
def crateListVByWord(word, vowels=['a', 'i', 'e', 'o', 'u']):
    """
    a function to return all vowels in a word
    :param word: the word
    :param vowels: all vowels in english
    :return: a list with all vowels in the word
    """
    return [i for i in word if i.lower() in vowels]


# general method to create a list of something from a sentence by a "func"
def listOfSentence(line, func):
    """
    a function to create a list by a function
    :param line: the parameter we use
    :param func:  the function we use
    :return: a list by the function and the parameter
    """
    if len(line) == 0:
        return []
    return listOfSentence(line[:-1], func) + [func(line[-1])]


# method to create a list of letters from b-n a word
def createListbmByWord(word, vowels=['a', 'i', 'e', 'o', 'u']):
    """
    as function to return all the letters between a-m that don't a vowels
    :param word: the word
    :param vowels: a list with all vowels in english
    :return: a list with all letters between a-m that don't vowels
    """
    return [i for i in word if
            'm' >= i.lower() >= 'a' and i.lower() not in vowels]


# method to create a tuple from some lists
def enterToATuple(L, x=[]):
    """
    a function to insert  a list to a tuple
    :param L: the list to insert
    :param x: a helper list
    :return: the tuple
    """
    return tuple([L] + x)


# method to create a list of letters from a-m a word
def createListnzByWord(word, vowels=['a', 'i', 'e', 'o', 'u']):
    """
    as function to return all the letters between n-z that don't a vowels
    :param word: the word
    :param vowels: a list with all vowels in english
    :return: a list with all letters between n-z that don't vowels
    """
    return list([i for i in word if
                 'z' >= i.lower() >= 'n' and i.lower() not in vowels])


# method to create a dictionary
def createDic(keys, values, dic):
    """
    a function to create a dictionary
    :param keys: the keys for the dictionary
    :param values: the values for the dictionary
    :param dic: the dic we insert into
    :return: dic
    """
    if len(keys) == 0:
        return dic
    dic[keys[0]] = values[0]
    return createDic(keys[1:], values[1:], dic)


# 'פונקציות לסעיף ב
#
def treatTxtFile(flName, merge=[]):
    """
    a general function to manage the whole text
    :param flName: the path of the file
    :param merge: an empty list
    :return: with the tuples we got
    """
    with open(flName, 'r') as f:
        for line in f:
            merge.append(treatLine(checkAllLetters(line), line))
        f.close()
    return merge


#  
def sikumofayim1(fldict, vals=[]):
    """
    a function to summarize all appearances in every line
    :param fldict: the dictionary we got
    :param vals: an empty list for help
    :return: a list with summarized appearances
    """
    vals = list(fldict.values())
    orgnizedList = list(zip(*[item for item in vals]))
    return [sum([len(orgnizedList[0][i]) for i in range(0, len(orgnizedList[0]))]),
            sum([len(orgnizedList[1][i]) for i in range(0, len(orgnizedList[1]))]),
            sum([len(orgnizedList[2][i]) for i in range(0, len(orgnizedList[2]))])]


#
def sumAll(fldict):
    """
    a function to sum all appearances
    :param fldict: the dictionary we got
    :return:  a list with the summarize
    """
    if len(fldict) == 0:
        return []
    return sumAll(fldict[:-1]) + sikumofayim1(fldict[-1][1])


#
def sikumofayim(fldict):
    listSum = sumAll(fldict)
    return [sum([listSum[i] for i in range(0, len(listSum), 3)]),
            sum([listSum[i] for i in range(1, len(listSum), 3)]),
            sum([listSum[i] for i in range(2, len(listSum), 3)]),
            sum([listSum[i] for i in range(0, len(listSum))])]


#
def createingOneTuple(l):
    if len(l) == 0:
        return []
    return createingOneTuple(l[:-1]) + l[-1]


#
def printingAll(fldict):
    return list([print(
        f"sentence: {list(fldict[i][1].keys())} LineNr:{fldict[i][0]} nr of vowels: {createingOneTuple(list(zip(*[item for item in list(fldict[i][1].values())]))[0])} nr of b-m consonants:{createingOneTuple(list(zip(*[item for item in list(fldict[i][1].values())]))[1])}nr of n-z consonants:{createingOneTuple(list(zip(*[item for item in list(fldict[i][1].values())]))[2])}")
        for i in range(0, len(fldict))])


#
def main():
    line = "This is an example"
    # print(treatLine(checkAllLetters(line),line))
    # print()
    # line1 = "t4his is an example"
    # print(treatLine(checkAllLetters(line1),line1))
    x = treatTxtFile("myDay.txt")
    # print(x)
    x.remove(x[-1])
    # print((sumAll(x[:-1])))
    print(sikumofayim(x[:-1]))
    print(printingAll(x[:-1]))


main()
