from functools import reduce


def digits(number):
    return reduce(lambda x, y: int(x) + int(y), [i for i in str(number)])


def main():
    print(digits(890))


if __name__ == '__main__':
    main()
