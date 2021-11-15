"""EX 2.6 protocol implementation
   Author: Maor Sarusi
   Date: 11/11/2020
"""

import time
import random

LENGTH_FIELD_SIZE = 2
PORT = 8820

# a list of commands to check if the client sends good command
cmd_list = ['RAND', 'NAME', 'TIME', 'EXIT']

rand_list = ["011", "012", "013", "014", "015", "016", "017", "018", "019", "0210"]

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def check_number(number):
    """
    function check_number gets a string and checks if it a  number or not
    :param number: the string
    :return: True if it a number and False if it didn't
    """
    if number == "":
        return False
    for i in number:
        if i not in DIGITS:
            return False
    return True


def check_cmd(data):
    """
     function check_cmd Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)
    :param data: the data the client send that he wants
    :return: True if it in the list and False if didn't
    """
    if data not in cmd_list:
        return False
    return True


def create_msg(data):
    """
   function create_msg Create a valid protocol message, with length field
    :param data: the data that the client sent to the server
    :return: the length of the data + the data as a string
    """
    length = str(len(data))
    if int(length) < 10:
        length = "0" + length
    return length + data


def get_msg(my_socket):
    """
    function get_msg Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    :param my_socket: the socket that the data throws in it (length + message)
    :return: a tuple with (True, the data) without the length if it by the protocol
             or (False, "ERROR") if it didn't
    """
    length = int(my_socket.recv(LENGTH_FIELD_SIZE).decode())
    if not check_number(str(length)):
        validation = False
        message = "ERROR"
    else:
        message = my_socket.recv(length).decode()
    if length != len(message):
        validation = False
        message = "ERROR"
    else:
        validation = True
    return validation, message


def create_server_rsp(cmd):
    """
   function create_server_rsp  Based on the command, create a proper response
    :param cmd: the command that the client wants from the server
    :return:    the server response to the command
    """
    if cmd == "RAND":
        response = str(random.randint(1, 10))
    elif cmd == "NAME":
        response = "Maor Sarusi's server"
    else:
        response = time.ctime()
    return create_msg(response)


# main function exists just for the asserts function
def main():
    #  asserts for protocol function

    # assert for check_number function
    assert check_number("10") is True
    assert check_number("3eer") is False
    assert check_number("1234r") is False

    # assert for check_cmd function
    assert check_cmd("RAND") is True
    assert check_cmd("NAME") is True
    assert check_cmd("TIME") is True
    assert check_cmd("EXIT") is True
    assert check_cmd("WWW") is False

    # assert for create_msg function
    assert create_msg("RAND") == "04RAND"
    assert create_msg("MAOR SARUSI") == "11MAOR SARUSI"

    # assert for create_server_rsp
    assert create_server_rsp("RAND") in rand_list
    assert create_server_rsp("TIME") == "24" + time.ctime()
    assert create_server_rsp("NAME") == "20Maor Sarusi's server"

    print("all asserts was good!!!")


if __name__ == "__main__":
    main()
