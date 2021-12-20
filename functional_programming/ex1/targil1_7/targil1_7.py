symbols = [".", ",", "?", "!", "(", ")", "[", "]", "{"]

def enterOneWord(word, dictionary):
    """
    a function that get a word and counting it in dictionary
    :param word: the word we got
    :param dictionary: the dictionary
    :return: the dictionary with the word
    """
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    return dictionary


#
# תכנית ראשית
def main():
    dictionary = {}
    with open('./shakespeare.txt', 'r', ) as f:
        for line in f:
            words = line.split()
            for word in words:
                if word[len(word) - 1] in symbols:
                    word = word[0:len(word) - 1]
                    enterOneWord(word, dictionary)
                else:
                    enterOneWord(word, dictionary)

    for keys, values in dictionary.items():
        print("the word: " + "'" + keys + "'" + " appears " + str(values) + " times")


if __name__ == '__main__':
    main()