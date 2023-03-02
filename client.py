# Task 2 Making a web client to test my server

import socket

HOST = 'localhost'  # Testing from the same computer. Then I can use 'localhost' or 127.0.0.1
PORT = 8000  # Servers port number

# Create a TCP socket to establish a connection between the client and the server over the internet og a network.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send an HTTP request to the server
request = 'GET /index.html HTTP/1.1.\r\nHost: {}\r\n\r\n'.format(HOST)

# Sending the request including the request message.
# We encode the message since the HTTP request is a string and the socket transmits binary data
client_socket.send(request.encode())

# receive the response
response = client_socket.recv(1024).decode()

# print the response
print(response)

# close the socket
client_socket.close()