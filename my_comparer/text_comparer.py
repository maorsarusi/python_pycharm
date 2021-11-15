FILE1 = r"C:\input.txt"
FILE2 = r"C:\expected.txt"
import sys

#FILE1 = 1
#FILE2 = 2


def compare(line1,name1,  line2, name2,  line_number):
    flag = True
    length = len(line1)
    length1 = len(line2)
    biggest = length1
    smallest = length
    if length > length1:
        biggest = length
        smallest = len(line2)
    for i in range(biggest):
        if i > smallest - 1 and smallest == length1:
            print("from character number {} in line number {} in {} the text is finished and in {} it is '{}'".format(i + 1,line_number,name2,name1, line1[i:]))
            return False
        elif  i > smallest - 1 and smallest == length:
            print("from character number {} in line number {} in {} the text is finished and in {} it is '{}'".format(i + 1,line_number,  name1,name2, line2[i:]))
            return False
        if line1[i] != line2[i]:
            character1 = line1[i]
            character2 = line2[i]
            if character1 == ' ':
                character1 = "space"
            if character2 == ' ':
                character2 = "space"
            print(
                "in line {} the character number {} in {} is '{}' and in {} is '{}'".format(line_number,
                                                                                                           i + 1,
                                                                                                           name1,
                                                                                                           character1,
                                                                                                           name2,
                                                                                                           character2))
            flag = False

    return flag


def comparer(text1, name1,  text2, name2):
    check = []
    for i in range(len(text1)):
        check += [compare(text1[i],name1,  text2[i], name2, i + 1)]
    if all(check):
        print("Compared succeed\n")


def check_format(path1, path2):
    format1 = path1.split('.')[-1]
    format2 = path2.split('.')[-1]
    print("format 1: {}, format 2: {} ".format(format1, format2))
    if format1 == format2:
        return True
    return False


def main():
    my_input = []
    expected = []
   # path1 = sys.argv[FILE1]
   # path2 = sys.argv[FILE2]
    path1 = FILE1
    path2 = FILE2
    name1 = path1.split('\\')[-1]
    name2 = path2.split('\\')[-1]
    if not check_format(name1, name2):
        print("The format aren't equals\n")
        return
    with open(path1, "r") as f:
        for line in f:
            if line[-1] == "\n":
                my_input += [line[:-1]]
            else:
                my_input += [line]
    with open(path2, "r") as f:
        for line in f:
            if line[-1] == "\n":
                expected += [line[:-1]]
            else:
                expected += [line]
    len_input = len(my_input)
    len_expected = len(expected)
    if len_input != len_expected:
        print("The length aren't equals\n")
        return
    comparer(my_input, name1, expected, name2)
    return


if __name__ == '__main__':
    main()
