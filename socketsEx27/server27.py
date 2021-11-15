#   Ex. 2.7 template - server side
#   Author: Maor Sarusi, 2020
#   Modified for Python 3, 2020

import socket
from socketsEx27 import protocol
import pyautogui
import os
import subprocess
import shutil
import glob
import time

# lists to define the commands by the parameters
list_one_parameter = ['SEND_FILE', 'DELETE', 'EXECUTE', 'DIR']
list_zero_parameters = ['TAKE_SCREENSHOT', 'EXIT']

# const vars
IP = "0.0.0.0"
PATH_FOR_SCREEN_SHOT = r'C:\Network\work\socketsEx27\screenPhoto.jpg'
FILE_NAME_PATH = r"C:\Network\work\socketsEx27\screenShotFile.txt"


def check_client_request(cmd):
    """
    Break cmd to command and parameters
    Check if the command and params are good.

    For example, the filename to be copied actually exists

    Returns:
        valid: True/False
        command: The requested cmd (ex. "DIR")
        params: string of the cmd params (ex. "c:\\cyber")
                or list of strings (ex. ["c:\\cyber1", "c:\\cyber2"])

    """
    # Use protocol.check_cmd first
    validation = protocol.check_cmd(cmd)
    if validation:
        # Then make sure the params are valid
        split_list = cmd.split(" ")
        if split_list[0] in list_one_parameter:
            flag = os.path.exists(split_list[1])
            return flag, split_list[0], split_list[1]
        elif split_list[0] in list_zero_parameters:
            return True, split_list[0], None
        elif split_list[0] == "COPY":
            if os.path.exists(split_list[1]):
                if split_list[1] != split_list[0]:
                    return True, split_list[0], [split_list[1], split_list[2]]
                else:
                    return False, "the path are equals", cmd
    return validation, "not a good command", cmd


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_FILE, only the length of the file will be sent (the data itself will be sent afterwards)

    Returns:
        response: the requested data
    """
    response = ""
    if command == 'TAKE_SCREENSHOT':
        if os.path.exists(PATH_FOR_SCREEN_SHOT):
            response = protocol.create_msg("the screenShot path is already exist ")
        else:
            image = pyautogui.screenshot()
            image.save(PATH_FOR_SCREEN_SHOT)
            response = protocol.create_msg("what a screen shot")
    elif command == 'EXECUTE':
        subprocess.call(params[0:])
        response = protocol.create_msg("you asked to execute: " + params[0:])
    elif command == 'DELETE':
        os.remove(params[0:])
        response = protocol.create_msg("you asked to delete: {} and you succeeded".format(params[0:]))
    elif command == 'DIR':
        x = params
        path = x + r"\*.*"
        file_list = glob.glob(path)
        files = "\n"
        for i in file_list:
            files += i + "\n"
        file_list = ""
        for i in files:
            i.split("\\")
            file_list += i[-1]
        response = protocol.create_msg("the files in the folder: {} are: {}".format(params, file_list))
    elif command == "SEND_FILE":
        print("you asked to send the screen shot\n")
        length = str(os.path.getsize(params))
        response = protocol.create_msg(length)
    elif command == "COPY":
        if params[0] == params[1]:
            response = protocol.create_msg("the files name are equals")
        elif params[0][protocol.find_last(params[0], '.') + 1:] != params[1][protocol.find_last(params[1], '.') + 1:]:
            response = protocol.create_msg("the file type isn't equals")
        else:
            shutil.copy(params[0], params[1])
            response = protocol.create_msg("you copy the file {} and you succeeded".format(params[0]))

    return response


def main():
    # asserts for server functions

    # assert for check_client_request function
    assert check_client_request("TAKE_SCREENSHOT") == (True, "TAKE_SCREENSHOT", None)
    assert check_client_request('SEND_FILE x') == (False, 'SEND_FILE', 'x')
    assert check_client_request("COPY x y") == (True, 'not a good command', 'COPY x y')

    # assert for handle_client_request function

    # depends if the photo exists or not
    # assert handle_client_request("TAKE_SCREENSHOT", None) == "0037the screenShot path is already exist"
    # assert handle_client_request("EXECUTE",
    #                             "C:\\Windows\\notepad.exe") == "0044you asked to execute: C:\\Windows\\notepad.exe"

    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    # handle requests until user asks to exit
    while True:
        # Check if protocol is OK, e.g. length field OK
        valid_protocol, cmd = protocol.get_msg(client_socket)
        if valid_protocol:
            # Check if params are good, e.g. correct number of params, file name exists
            valid_cmd, command, params = check_client_request(cmd)
            if valid_cmd:
                if command == 'EXIT':
                    break

                # prepare a response using "handle_client_request"
                request = handle_client_request(command, params)

                # send to client
                client_socket.send(request.encode())

                if command == "SEND_FILE":
                    array_bytes = bytearray()
                    with open(params, "rb") as file:
                        for i in file:
                            array_bytes += i

                    client_socket.send(array_bytes)

            else:
                # prepare proper error to client
                response = 'Bad command or parameters'
                # send to client
                client_socket.send(protocol.create_msg(response).encode())

        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            # send to client
            client_socket.send(response.encode())
            # Attempt to clean garbage from socket
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
