import socket
my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 80))
print('I am connected')
input()
