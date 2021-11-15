import random


def who_bigger(f1, f2):
    if f1.get_mechane == f2.get_mechane:
        if f1.get_mone > f2.get_mone:
            return "{} is bigger than {}".format(f1.get_fraction(), f2.get_fraction())
        elif f1.get_mone < f2.get_mone:
            return "{} is bigger than {}".format(f2.get_fraction(), f1.get_fraction())
        else:
            return "fraction is equals"
    else:
        mone1 = f1.get_mone()
        mechane1 = f1.get_mechane()
        mone2 = f2.get_mone()
        mechane2 = f2.get_mechane()
        f1_new = fraction(mone1, mechane1)
        f2_new = fraction(mone2, mechane2)
        f1_new.set_mechane(mechane1 * mechane2)
        f2_new.set_mechane(mechane1 * mechane2)
        f1_new.set_mone(mone1 * mechane2)
        f2_new.set_mone(mechane1 * mone2)
        if f2_new.get_mone() < f1_new.get_mone():
            return "{} is bigger than {}".format(f1.get_fraction(), f2.get_fraction())
        elif f1_new.get_mone() < f2_new.get_mone():
            return "{} is bigger than {}".format(f2.get_fraction(), f1.get_fraction())
        else:
            return "fractions equals"


def calc_fraction(f1, f2, op):
    if op == "+":
        return f1.add_fraction(f2)
    if op == "-":
        return f1.sub_fraction(f2)
    if op == "*":
        return f1.mul_fraction(f2)
    if op == ":":
        return f1.div_fraction(f2)


class fraction:
    def __init__(self, mone, mechane):
        if mechane != 0:
            self.__mone = mone
            self.__mechane = mechane
            print("הכנסת כמונה {} וכמכנה {}".format(mone, mechane))
        else:
            print("ניסית להכניס כמונה {} וכמכנה 0".format(mone))
            print("המכנה לא יכול להיות 0 ולכן ברירת המחדל היא 1")
            self.__mone = mone
            self.__mechane = 1
        self.pick_minus()

    def print_fraction(self):
        meaning = self.check_meaning()
        if meaning == -1:
            fraction = "{}/{}".format(self.__mone, self.__mechane)
            print(fraction)
        else:
            print(meaning)

    def get_fraction(self):
        meaning = self.check_meaning()
        if meaning == -1:
            fraction = "{}/{}".format(self.__mone, self.__mechane)
            return fraction
        else:
            return meaning

    def get_mone(self):
        return self.__mone

    def get_mechane(self):
        return self.__mechane

    def set_mone(self, mone):
        self.__mone = mone

    def set_mechane(self, mechane):
        self.__mechane = mechane

    def reduce(self):
        old_mone = self.__mone
        if old_mone < 1:
            old_mone *= -1
        for i in range(old_mone, 1, -1):
            if self.__mone % i == 0 and self.__mechane % i == 0:
                self.__mone = int(self.__mone / i)
                self.__mechane = int(self.__mechane / i)
        return self.pick_minus()

    def add_fraction(self, f1):
        old_mone = self.__mone
        old_mechane = self.__mechane
        if f1.get_mechane() == self.get_mechane():
            self.__mone = int(f1.get_mone() + self.get_mone())
            self.__mechane = f1.get_mechane()
        elif f1.get_mechane() % self.get_mechane() == 0:
            self.__mone = int(f1.get_mone() + self.get_mone() * (f1.get_mechane() / self.get_mechane()))
            self.__mechane = f1.get_mechane()
        elif self.get_mechane() % f1.get_mechane() == 0:
            self.__mone = int(self.get_mone() + f1.get_mone() * (self.get_mechane() / f1.get_mechane()))
            self.__mechane = self.get_mechane()
        else:
            self.__mone = int(f1.get_mone() * self.get_mechane() + self.get_mone() * f1.get_mechane())
            self.__mechane = f1.get_mechane() * self.get_mechane()
        self.reduce()
        print("{}/{} + {} = {}".format(old_mone, old_mechane, f1.get_fraction(), self.get_fraction()))
        return self

    def mul_fraction(self, f1):
        old_mone = self.__mone
        old_mechane = self.__mechane
        self.__mone *= f1.get_mone()
        self.__mechane *= f1.get_mechane()
        self.reduce()
        print("{}/{} * {} = {}".format(old_mone, old_mechane, f1.get_fraction(), self.get_fraction()))
        return self

    def sub_fraction(self, f1):
        old_mone = self.__mone
        old_mechane = self.__mechane
        if f1.get_mechane() == self.get_mechane():
            self.__mone = int(f1.get_mone() - self.get_mone())
            self.__mechane = f1.get_mechane()
        elif f1.get_mechane() % self.get_mechane() == 0:
            new_self_mone = int(self.get_mone() * (f1.get_mechane() / self.get_mechane()))
            new_mone = new_self_mone - f1.get_mone()
            self.__mone = new_mone
            self.__mechane = f1.get_mechane()
        elif self.get_mechane() % f1.get_mechane() == 0:
            self.__mone = int(self.get_mone() - f1.get_mone() * (self.get_mechane() / f1.get_mechane()))
            self.__mechane = self.get_mechane()
        else:
            self.__mone = int(f1.get_mone() * self.get_mechane() - self.get_mone() * f1.get_mechane())
            self.__mechane = f1.get_mechane() * self.get_mechane()
        self.reduce()
        print("{}/{} - {} = {}".format(old_mone, old_mechane, f1.get_fraction(), self.get_fraction()))
        return self

    def div_fraction(self, f1):
        old_mone = self.__mone
        old_mechane = self.__mechane
        self.__mone *= f1.get_mechane()
        self.__mechane *= f1.get_mone()
        self.reduce()
        print("{}/{} : {} = {}".format(old_mone, old_mechane, f1.get_fraction(), self.get_fraction()))
        return self

    def pick_minus(self):
        x = self.get_mone()
        y = self.get_mechane()
        if (x > 0 and y < 0) or (x < 0 and y < 0):
            self.set_mone(self.get_mone() * -1)
            self.set_mechane(self.get_mechane() * -1)
        return self

    def check_meaning(self):
        if self.get_mone() == 0:
            return 0
        elif self.get_mone() == self.get_mechane():
            return 1
        elif self.get_mechane() == 1:
            return self.get_mone()
        return -1


def main():
    while True:
        x = fraction(7, 3)
        y = fraction(1, 4)
        print(x.mul_fraction(y).get_fraction())
        rand = input("האם תרצה להגריל מונה ומכנה?{}".format("\n"))
        if rand == "לא":
            break
        elif rand == "כן":
            mone = random.randint(0, 10)
            mechane = random.randint(0, 10)
            fraction1 = fraction(mone, mechane)
            mone = random.randint(0, 10)
            mechane = random.randint(0, 10)
            fraction2 = fraction(mone, mechane)
            fraction1.print_fraction()
            fraction2.print_fraction()
            print(who_bigger(fraction1, fraction2))
            operator = input("איזה פעולה תרצה לבצע עם השברים? +-*/ או צמצום{}".format("\n"))
            while True:
                if operator == "צ":
                    fraction1.reduce()
                    fraction2.reduce()
                    fraction1.print_fraction()
                    fraction2.print_fraction()
                    break
                elif operator == "+":
                    fraction1.add_fraction(fraction2)
                    break
                elif operator == "-":
                    fraction1.sub_fraction(fraction2)
                    break
                elif operator == "*":
                    fraction1.mul_fraction(fraction2)
                    break
                elif operator == "/":
                    fraction1.div_fraction(fraction2)
                    break
                else:
                    print("פעולה לא חוקית")
        else:
            print("תשובה לא חוקית")


if __name__ == '__main__':
    main()
