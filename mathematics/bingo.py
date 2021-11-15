import random
import sys

FILE = r"C:\Network\work\decimal_fraction\exercises.txt"

def main():
    list_exe = []
    list_result = []
    split_list = []
    num_list = []

    with open(FILE, "r") as f:
        for i in f:
            split_list = i.split("=")
            split_list[1] = split_list[1][0:-1]
            list_exe += [split_list[0]]
            list_result += [split_list[1]]
    num = random.randint(0, 33)
    num_list += [num]
    for i in range(33):
        num = random.randint(0, 33)
        while num in num_list:
            num = random.randint(0, 33)
        num_list += [num]
    for i in num_list:
        print("{} = {}".format(list_exe[i], list_result[i]))
        x = input("continue or exit? c/x\n")
        if x == "c":
            continue
        elif x == "x":
            break


if __name__ == "__main__":
    main()
