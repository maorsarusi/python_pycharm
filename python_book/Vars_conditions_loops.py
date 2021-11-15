__author__ = "Maor"


def baby1():
    for i in range(1, 41):
        print(i)
    return


def sevenBoom():
    for i in range(101):
        if i % 7 == 0 or (i - 7) % 10 == 0 or i // 10 == 7:
            print(i)
    return


def takeABreak():
    x = 1
    y = 1
    print(x)
    print(y)
    while True:
        if x + y < 10000:
            z = y
            y += x
            print(y)
            x = z
        else:
            break


def babyPampers():
    i = 0.0
    while True:
        if i <= 5.0:
            if i % 1 == 0.0:
                print(int(i))
            else:
                print(round(i, 1))
            i = round(i, 1) + 0.1
        else:
            break


def isPrime():
    flag = True
    for i in range(1, 201):
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0 and not i / j == 1:
                flag = False
                break
        if flag:
            print(i)
        else:
            flag = True


def main():
    print("the numbers between 1 - 40 are:")
    baby1()
    print()
    print("the number for the game seven boom is:")
    sevenBoom()
    print()
    print("the fibonacci to 10000")
    takeABreak()
    print()
    print("the numbers between 1-5 with jumps of 0.1:")
    babyPampers()
    print()
    print("the primes numbers between 1-200:")
    isPrime()
    return


if __name__ == '__main__':
    main()
