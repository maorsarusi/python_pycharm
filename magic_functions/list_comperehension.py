def avg(list1):
    return sum(list1) / len(list1)


def avg_diff(list1, list2):
    return avg([i - j for i in list1 for j in list2])


def anti_b(string):
    return "".join([i for i in string if i != 'b'])

def main():
    list1 = [1, 2, 3, 4]
    list2 =  [1, 1, 1, 1]
    string = "abanibi"
    print("the avg diff of the 2 lists:{} ,{} are: {}".format(list1, list2, avg_diff(list1, list2)))
    print("the string: {} without b's is: {} ".format(string, anti_b(string)))


if __name__ == "__main__":
    main()
