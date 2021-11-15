import random


class Dice:
    def __init__(self, num_of_dice):
        self.__number = self.get_result()
        self.__num_of_dice = num_of_dice

    def get_number(self):
        return self.__number

    def get_num_of_dice(self):
        return self.__num_of_dice

    def __str__(self):
        return "קוביה מספר {}: תוצאה {}".format(self.get_num_of_dice(), self.get_number())

    def get_result(self):
        return random.randint(1, 6)

def main():

    dic1 = Dice(1)
    print(dic1)


if __name__ == "__main__":
    main()
