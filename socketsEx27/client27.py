#   Ex. 2.7 template - client side
#   Author: Maor Sarusi , 2020
#   Modified for Python 3, 2020


import socket
from socketsEx27 import protocol
import os

IP = "127.0.0.1"
PATH_FOR_SEND_FILE = r"C:\Network\work\socketsEx27\send_file.jpg"


def handle_server_response(my_socket, cmd):
    """
    Receive the response from the server and handle it, according to the request

    For example, DIR should result in printing the contents to the screen,
    while SEND_FILE should result in saving the received file and notifying the user

    Note- special attention should be given to SEND_FILE as if may require several receives
    """
    only_cmd = cmd.split(" ")[0]
    if only_cmd == 'EXIT':
        print("you exit from the server\n")
        return
    valid, response = protocol.get_msg(my_socket)
    if only_cmd == 'SEND_FILE':
        if not os.path.exists(PATH_FOR_SEND_FILE):
            file = my_socket.recv(int(response))
            with open(PATH_FOR_SEND_FILE, 'ab') as send_file:
                send_file.write(file)
            response = "the file sent good!"
        else:
            response = "the file is already sent before"
    print(response)
    return


def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, protocol.PORT))

    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_FILE\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')

    # loop until user requested to exit
    while True:
        cmd = input("Please enter command:\n")
        if protocol.check_cmd(cmd):
            packet = protocol.create_msg(cmd)
            my_socket.send(packet.encode())
            if cmd == 'EXIT':
                break
            handle_server_response(my_socket, cmd)
        else:
            print("Not a valid command, or missing parameters\n")

    # close socket
    my_socket.close()
    print("socket disconnected")


if __name__ == '__main__':
    main()
