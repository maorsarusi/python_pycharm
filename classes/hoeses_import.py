from classes import Horses


def main():
    Bin = Horses.Horse("Bin", 5)
    print(Bin)
    unknown = Horses.Horse()
    print(unknown)
    unknown.set_birthday()
    unknown.set_name("Sean")
    print(unknown)


if __name__ == '__main__':
    main()
