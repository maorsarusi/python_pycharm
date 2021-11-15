PATH = "shoplist"


def main():
    with open(PATH, 'r') as file:
        data = file.read()
    split_data = data.split("#")
    print(split_data)
    split_by_name = []
    for l in split_data:
        split_by_name += [l.split(":")]
    names = []
    prod_list = []
    for l in split_by_name:
        names += [l[0]]
        prod_list += [l[1]]
    amount = []
    for l in prod_list:
        amount += [l.split(',')]
    print(amount)




if __name__ == "__main__":
    main()
