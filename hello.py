def hello(name):
    return 'hello ' + name


def main():
    name = input("הכ:\n")
    print(hello(name))
    out = input("want to exit? y/n?\n")
    while out != "y":
        if out == "y":
            break
        out = input("want to exit? y/n\n?")


if __name__ == '__main__':
    main()
