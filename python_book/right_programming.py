__author__ = "Maor"

# a list exist to easy check if the input are number
LIST_OF_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# the length of the number
LENGTH = 5


def is_number(num):
    """
    function is_number gets a string and checks if it a number
    :param num: the string that we check
    :return: True if the string made only from numbers and False if didn't
    """
    if num == "":
        return False
    for i in num:
        if i not in LIST_OF_DIGITS:
            return False
    return True


def user_insert(insert_number):
    """
    function user_insert gets a string and checks if it a number
    :param insert_number: the string we got
    :return: True if it number and false if didn't
    """
    if not is_number(insert_number):
        return False
    else:
        return True


def digits(number):
    """
    function digits gets a number and return a string of its digits
    separated by ','
    :param number: the number we got
    :return: new string with the digits of the number
    """
    digits_number = ""
    for i in number:
        digits_number += (i + ",")
    return digits_number[:-1]  # we took the string without the last char because it is ','


def sum_digits(digits_string):
    """
    function sum_digits gets a number and summarize its digits
    :param digits_string: string  of  digits
    separated by ','
    :return: the summarize of the number
    """
    sum_of_digits = 0
    digits_string = digits_string.split(",")  # splitting the string by the ','
    for i in digits_string:
        sum_of_digits += int(i)
    return sum_of_digits


def dejavu(number):
    """
    function dejavu gets a number and return its digits an its sum of digits
    :param number: the number we got from the user
    :return: a string with its digits separated by ','  and the sum of its digits
    """
    digits_string = digits(number)
    sum_of_digits = sum_digits(digits_string)
    return digits_string, sum_of_digits


def main():
    # asserts for the function

    # asserts for user_insert function
    assert user_insert("") is False
    assert user_insert("12345") is True
    assert user_insert("1111") is True

    # asserts for is_number function
    assert is_number("11223") is True
    assert is_number("a1121") is False
    assert is_number("111111111") is True  # True by the function but need to be false by the exc

    # asserts for digits function
    assert digits("12345") == "1,2,3,4,5"
    assert digits("99999") == "9,9,9,9,9"

    # asserts for sum_digits function
    assert sum_digits("1,2,3,4,5") == 15
    assert sum_digits("9,9,9,9,9") == 45

    # asserts for dejavu function
    assert dejavu("12345") == ("1,2,3,4,5", 15)
    assert dejavu("98765") == ("9,8,7,6,5", 35)

    while True:
        insert_number = input("enter a number with 5 digits, must be a number!\n")
        if not user_insert(insert_number):
            print("you need to insert a number")
        elif len(str(insert_number)) != LENGTH:
            print("length must be {}".format(LENGTH))
        else:
            digits_string, sum_of_digits = dejavu(insert_number)
            print(" the number is: {}\n it digits are: {}\n and the sum of it digits are: {}".format(insert_number,
                                                                                                     digits_string,
                                                                                                     sum_of_digits))
            break


if __name__ == '__main__':
    main()
