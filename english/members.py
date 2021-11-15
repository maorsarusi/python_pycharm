ones = ["c", "i", "j", "k", "o", "p", "s", "u", "v", "x", "z"]
twos = ["f", "h", "l", "m", "n", "r", "t", "w", "y"]
threes = ["a", "b", "d", "e", "g", "q"]
names = ["Shani", "Shaked", "Moshe", "Noa"]


def create_dic(one, two, three):
    cal_dic = {}
    for i in one:
        cal_dic[i] = 1
    for i in two:
        cal_dic[i] = 2
    for i in three:
        cal_dic[i] = 3
    return cal_dic


def calculate(name, dictionary):
    sum = 0
    for i in name:
        sum += dictionary[i]
    return sum


def main():
    shani = []
    shaked = []
    moshe = []
    noa = []
    cal_dict = create_dic(ones, twos, threes)
    while True:
        num_list = input("Insert the list to finish insert 0\n")
        if num_list == "0":
            break
        letter = input("Insert the letter\n")
        if num_list == "1":
            shani += [letter]
        elif num_list == "2":
            shaked += [letter]
        elif num_list == "3":
            moshe += [letter]
        else:
            noa += [letter]
    kids = [shani, shaked, moshe, noa]
    count = 0
    for i in kids:
        print("{}: sum: {}".format(names[count], calculate(i, cal_dict)))
        count += 1



if __name__ == "__main__":
    main()
