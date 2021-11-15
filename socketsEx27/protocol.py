#   Ex. 2.7 template - protocol
#   Author: Maor Sarusi, 2020
#   Modified for Python 3, 2020
LENGTH_FIELD_SIZE = 4
PORT = 8820

# a dictionary to command and number of parameters
COMMANDS = {'COPY': 2, 'SEND_FILE': 1, 'DIR': 1, 'DELETE': 1, 'EXECUTE': 1, 'TAKE_SCREENSHOT': 0, 'EXIT': 0}


def check_cmd(data):
    """
    function check_cmd checks if the command is defined in the protocol, including all parameters
    For example, DELETE c:\\work\file.txt is good, but DELETE alone is not
    :param data: the command we got
    :return: True if the command and the number of parameters are good
             and False if didn't
    """
    validation = True
    list_of_data = data.split(" ")
    if not list_of_data[0] in COMMANDS.keys():
        validation = False
    elif data == 'TAKE_SCREENSHOT' or data == 'EXIT':
        if not len(list_of_data) == 1:
            validation = False
    elif not len(list_of_data[1:]) == COMMANDS[list_of_data[0]]:
        validation = False
    return validation


def create_msg(data):
    """
    function  Create a valid protocol message, with length field
    :param data: the message we got
    :return: the message with the length in 4 bytes
            for example the message 'ab will be '0002ab'
    """
    length = str(len(data))

    return "0" * (4 - len(length)) + str(length) + data


def get_msg(my_socket):
    """
    function get_msg Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    :param my_socket: the socket we got
    :return: the message without the length field
    """
    length = my_socket.recv(LENGTH_FIELD_SIZE).decode()

    if not length.isdigit():
        validation = False
        message = "ERROR"
    else:
        length = int(length)
        message = my_socket.recv(length).decode()
    if length != len(message):
        validation = False
        message = "ERROR"
    else:
        validation = True
    return validation, message


def find_last(string, character):
    """
    function find_last gets a string and a character
    and returns the last time the the character appears in the string
    :param string: the string we check
    :param character: the character we looking for
    :return: the last appearance of character in string
    """
    return [i for i in range(len(string)) if string[i] == character][-1]


def main():
    # asserts for the function

    # assert for check_cmd function
    assert check_cmd("TAKE_SCREENSHOT") is True
    assert check_cmd("TAKE_SCREENSHOT AAA") is False
    assert check_cmd("SEND_FILE X") is True
    assert check_cmd("SEND_FILE") is False
    assert check_cmd("EXIT") is True
    assert check_cmd("EXIT S") is False
    assert check_cmd("DIR SSS") is True
    assert check_cmd("DIR") is False
    assert check_cmd("EXECUTE") is False
    assert check_cmd("EXECUTE FFF") is True
    assert check_cmd("COPY X Y") is True
    assert check_cmd("COPY D") is False

    # assert for create_msg function
    assert create_msg("RAND") == "0004RAND"
    assert create_msg("MAOR SARUSI") == "0011MAOR SARUSI"

    # assert for find_last function
    assert find_last("abxaaa", "a") == 5

    print("all asserts was good!!!")


if __name__ == '__main__':
    main()
