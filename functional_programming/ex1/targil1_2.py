#
#  Example program for Targil 1
#
import math


def isNumber(valStr):
    """
    a function to check if a string is a number
    :param valStr: the string to check
    :return: true if it a number and false if it didn't
    """
    if valStr.count('.') > 1:
        return False
    L = [c for c in valStr if (c.isdigit() or c == '.')]
    return len(L) == len(valStr)


#

def getNumber(prompt):
    """
    a function to check validation to a number
    :param prompt: the parameter
    :return: the parameter if it a number
    """
    while True:
        val = input(prompt)
        if not isNumber(val):
            print("it must be a number!")
        else:
            return eval(val)


def rectangleArea(w, h):
    """
    Area calculation program  rectangle
    :param w: width
    :param h: height
    :return:  the area
    """
    return w * h


#
def circleArea(r):
    """
    Area calculation program  circle
    :param r: radius
    :return: the area
    """
    return math.pi * r ** 2


#
def sphereArea(r):
    """
    Area calculation program sphere
    :param r: radius
    :return: the area
    """
    val = math.pi * (4 / 3)
    return val * r ** 3


#
def coneArea(h, r):
    """
    Area calculation program cone
    :param h: height
    :param r: radius
    :return: the area
    """
    return h * (1 / 3) * math.pi * r ** 2


#
def squarePyramidArea(a, h):
    """
    Area calculation program  square pyramid
    :param a: the base
    :param h: height
    :return: the area
    """
    s = rectangleArea(a, a)
    return s * h * (1 / 3)


# printing the menu options
def prtMenu(shapes):
    for i in range(len(shapes)):
        print(i + 1, shapes[i])
    return


#
# main program
#
def main():
    print("Welcome to the Area calculation program")
    print("---------------------------------------\n")
    # Print out the menu
    shapes = ("Rectangle", "Circle", "Sphere", "Cone", "Square pyramid")
    while True:
        print("\nPlease select a shape (press 0 to quit):")
        prtMenu(shapes)
        # Get the user's choice:
        shape = input("> ")
        # Calculate the area:
        if shape == "1":
            height = eval(input("Please enter the height: "))
            width = eval(input("Please enter the width: "))
            area = rectangleArea(width, height)
            print("The area is", area)
            continue
        elif shape == "2":
            radius = eval(input("Please enter the radius: "))
            area = circleArea(radius)
            print("The area is", area)
            continue
        elif shape == "3":
            radius = eval(input("Please enter the radius: "))
            area = sphereArea(radius)
            print("The area is", area)
            continue
        elif shape == "4":
            radius = eval(input("Please enter the radius: "))
            height = eval(input("Please enter the height: "))
            area = coneArea(height, radius)
            print("The area is", area)
            continue
        elif shape == "5":
            width = eval(input("Please enter the width: "))
            height = eval(input("Please enter the height: "))
            area = squarePyramidArea(width, height)
            print("The area is", area)
            continue
        elif shape == "0":
            print("Bye!")
            break
        else:
            print("Invalid shape")


if __name__ == "__main__":
    main()
