class BigThings:
    def __init__(self, param):
        self.__param = param

    def size(self):
        if isinstance(self.__param, int) or isinstance(self.__param, float):
            return self.__param
        elif isinstance(self.__param, list) or isinstance(self.__param, dict) or isinstance(self.__param, str):
            return len(self.__param)

    def get_param(self):
        return self.__param


class BigCat(BigThings):
    def __init__(self, name, weight):
        super(BigCat, self).__init__(name)
        self.__weight = weight

    def size(self):
        if isinstance(self, BigCat):
            if 15 < self.__weight < 20:
                return "the cat {} is fat".format(self.get_param())
            elif self.__weight >= 20:
                return "the cat {} is very fat".format(self.get_param())
            else:
                return "the cat {} is ok".format(self.get_param())


def main():
    thing = BigThings(6)
    print(thing.size())
    thing1 = BigThings("maor amos")
    print(thing1.size())

    cat = BigCat("latif", 55)
    cat1 = BigCat("Mitzi", 16)
    cat2 = BigCat("Tom", 10)

    print(cat.size())
    print(cat1.size())
    print(cat2.size())


if __name__ == '__main__':
    main()
