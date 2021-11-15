# Ex 4.4 - HTTP Server Shell
# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import socket
import os

# TO DO: set constants
IP = "0.0.0.0"
PORT = 80
SOCKET_TIMEOUT = 0.1
WEBROOT = r"C:\Network\work\Ex44\webroot"
DEFAULT_URL = "\index.html"
REDIRECTION_DICTIONARY = {"/forbidden.html": "403", "/page1.html": "302",
                          "Internal Server Error": '500'}
FILE_TYPES_DICTIONARY = {'html': "ContentType: text/html; charset=utf 8", 'jpg': "ContentType: image/jpeg",
                         'js': "ContentType: text/javascript; charset=UTF 8", 'css': "ContentType: text/css"}
VERSION = "HTTP/1.1"
OK = " 200 OK\r\n"


def get_file_data(filename):
    """
    function get_file_data gets a file name
    and returns a tuple of answer if the file exist and the file
    :param filename: the path of the file(without webroot)
    :return: True, the file if it exist
             False, "" if it didn't
    """
    data = ""
    path = WEBROOT + filename
    if os.path.isfile(path):
        with open(path, "rb") as file:
            data = file.read()
        return True, data
    return False, ""


def handle_client_request(resource, client_socket):
    """
    function handle_client_request gets a resource and a socket
    and send the request
    :param resource: URL  and parameters
    :param client_socket: the socket that we send the response
    """
    # TO DO : add code that given a resource (URL and parameters) generates the proper response
    if resource == '/':
        url = DEFAULT_URL
    else:
        url = resource
    validation, data = get_file_data(url)
    # TO DO: check if URL had been redirected, not available or other error code. For example:
    if url in REDIRECTION_DICTIONARY:
        # TO DO: send 302 redirection response
        if REDIRECTION_DICTIONARY[url] == "302":
            if validation:
                client_socket.send(("{} {} Moved Temporarily\r\n ".format(VERSION, REDIRECTION_DICTIONARY[url]) +
                                    "Content-Type: text/html; charset=utf-8\r\n" +
                                    "Content-Length: " + str(len(data)) + "\r\n\r\n").encode() + data)

        elif REDIRECTION_DICTIONARY[url] == "403":
            client_socket.send(("{} {} forbidden\r\n".format(VERSION, REDIRECTION_DICTIONARY[url])).encode())
        return
    elif not validation:
        client_socket.send("{} 404 not found\r\n\r\n".format(VERSION).encode())
        return
    filetype = url.split(".")[-1]
    http_header = VERSION + OK
    # TO DO: extract requested file tuple from URL (html, jpg etc)
    if filetype == 'html':
        http_header += FILE_TYPES_DICTIONARY['html'] + "\r\n" + "Content-Length: " + str(len(data)) + "\r\n\r\n"
    elif filetype == 'jpg' or filetype == 'ico':
        http_header += FILE_TYPES_DICTIONARY['jpg'] + "\r\n" + "Content-Length: " + str(len(data)) + "\r\n\r\n"
    # TO DO: handle all other headers
    elif filetype == 'css':
        http_header += FILE_TYPES_DICTIONARY['css'] + "\r\n" + "Content-Length: " + str(len(data)) + "\r\n\r\n"
    elif filetype == 'js':
        http_header += FILE_TYPES_DICTIONARY['js'] + "\r\n" + "Content-Length: " + str(len(data)) + "\r\n\r\n"

    http_response = http_header.encode() + data
    client_socket.send(http_response)


def validate_http_request(request):
    """
    function validate_http_request gets a request and checks if it valid
    :param request: the request we got
    :return: tuple of validation of the request and the url extract from the request(if the request valid)
    """
    request_list = request.decode().split(" ")
    method = "GET"
    version = "HTTP/1.1\r\nHost:"
    url = ""
    validation = False
    if request_list[0] == method:
        if request_list[2] == version:
            url = request_list[1]
            validation = True
    return validation, url


def handle_client(client_socket):
    """
    function handle_client check if the request from the client is legal and handle it
    :param client_socket: the socket of the client
    """
    print('Client connected')
    while True:
        client_request = client_socket.recv(1024)
        valid_http, resource = validate_http_request(client_request)
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
            error_number = '500'
            client_socket.send("{} {} {}\r\n".format(VERSION, error_number, REDIRECTION_DICTIONARY[error_number]))
            break
    print('Closing connection')
    client_socket.close()


def main():
    # Open a socket and loop forever while waiting for clients
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        # client_socket.settimeout(SOCKET_TIMEOUT)
        handle_client(client_socket)


if __name__ == "__main__":
    # Call the main handler function
    main()
