def filtering_me(number):
    return list(filter(lambda x: x % 3 == 0, [num for num in range(1, number + 1)]))


def main():
    print(filtering_me(10))


if __name__ == '__main__':
    main()
