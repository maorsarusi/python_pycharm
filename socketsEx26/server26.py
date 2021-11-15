"""EX 2.6 server implementation
   Author: Maor Sarusi
   Date: 11/11/2020
"""

import socket
from socketsEx26 import protocol


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        # Get message from socket and check if it is according to protocol
        valid_msg, cmd = protocol.get_msg(client_socket)
        if valid_msg:
            # 1. Print received message
            print("CLIENT SENT: {}".format(cmd))
            # 2. Check if the command is valid
            if protocol.check_cmd(cmd):
                # 3. If valid command - create response
                response = protocol.create_server_rsp(cmd)
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024).decode()  # Attempt to empty the socket from possible garbage
        # Handle EXIT command, no need to respond to the client
        if cmd == "EXIT":
            break

        # Send response to the client
        client_socket.send(response.encode())

    print("Server Closing\n")
    # Close sockets
    server_socket.close()
    client_socket.close()


if __name__ == "__main__":
    main()
