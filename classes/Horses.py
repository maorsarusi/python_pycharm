class Horse:

    def __init__(self, name="Unknown", age=0):
        self.__name = name
        self.__age = age

    def set_birthday(self):
        self.__age += 1

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return "the age of {} is: {}".format(self.__name, self.__age)

    def __str__(self):
        return "horse name: {}\nage: {}".format(self.__name, self.__age)


def main():
    Bin = Horse("Bin", 5)
    print(Bin.get_age())
    Bin.set_birthday()
    print(Bin.get_age())
    Sean = Horse("Sean", 7)
    print(Sean.get_age())
    unknown = Horse()
    print(unknown.get_age() + "\n")
    print(Bin)


if __name__ == "__main__":
    main()
