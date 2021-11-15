from scapy.all import *
import sys

# consts for the test
LENGTH = 9
IP_CLIENT = "192.168.1.12"
IP_SERVER = "192.168.1.12"
CLIENT_INPUT = 1


def clent_sending(client_input):
    """
    function clent_sending gets the input from the client and sens it
    to the server
    :param client_input:the input from the client

    """
    client_packet = IP(dst=IP_SERVER) / client_input
    try:
        send(client_packet, verbose=0)
        print("the send is succeeded")
    except TypeError:
        print("the send didn't go well")
    return


def add(num1, num2):
    """
    function add gets 2 number and sum them
    :param num1: the first number
    :param num2: the second number
    :return: the sum of num1 and num2
    """
    return num1 + num2


def subtract(num1, num2):
    """
    function subtract get 2 numbers and subtract them
    :param num1: the first number
    :param num2: the second number
    :return:     the subtraction between the 2 numbers
    """
    return num1 - num2


def multiply(num1, num2):
    """
    function multiply gets 2 numbers and multiply them
    :param num1:  the first number
    :param num2:  the second number
    :return:      the result of the multilation
    """
    return num1 * num2


def divide(num1, num2):
    """
    function divide gets 2 numbers and divide them
    :param num1: the first number
    :param num2: the second number
    :return:     the division if the first number is'nt 0
                 or an error message if it is
    """
    if num2 == 0:
        return "can't divide by 0"
    return num1 / num2


# a dictionary to manage the operation requests
operators_dictionary = {"+": add, "-": subtract, "/": divide, "*": multiply}


def check_validation(load):
    """
    function check_validation gets the raw we wants and check if it is validation
    :param load: the message we want to get
    :return: the parts of the message and True if the message is valid and nothing for the parts and false if it didn't
    """
    if len(load) != LENGTH:
        return "", "", "", False
    first_number = load[:4]
    second_number = load[4:-1]
    op = load[-1]
    if op not in operators_dictionary:
        return "", "", "", False
    else:
        if not first_number.isdigit() or not second_number.isdigit():
            return "", "", "", False
    return first_number, second_number, op, True


def just_our_packages(packages):
    """
    function just_our_packages filter the packages that we gets from the net
    to the packages that match to our requests
    :param packages: all the packages we gets
    :return:       a list with the
    """
    our_packages = []
    first_number = ""
    second_number = ""
    op = ""
    validation = False
    for package in packages:
        first_number, second_number, op, validation = check_validation(package[Raw].load.decode())
        if validation:
            our_packages += [(first_number, second_number, op)]
    return our_packages


def manange_result(packages):
    """
    function manange_result gets list of tuples and calculate the results
    :param packages: the packages that valid
    :return:
    """
    result_list = []
    for package in packages:
        first_number = int(package[0])
        second_number = int(package[1])
        op = package[2]
        result = operators_dictionary[op](first_number, second_number)
        result_list += [str(result)]
    return result_list

