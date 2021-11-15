import random


def main():
    l1 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    l2 = [0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.03, 0.02, 0.01, 0.00]
    while True:
        i1 = random.randint(0, 9)
        i2 = random.randint(0, 9)
        print("המספר הראשון שיצא הוא: {}".format(l1[i1]))
        print("המספר השני שיצא הוא :{}".format(l2[i2]))
        s = input("לדעת את הסכום?{}".format("\n"))
        if s == "כן":
            print(round(l1[i1] + l2[i2], 2))
        io = input("להמשיך? לחץ 0 או כן{}".format("\n"))
        print()
        if io != '0' and io != "כן":
            break


if __name__ == "__main__":
    main()
