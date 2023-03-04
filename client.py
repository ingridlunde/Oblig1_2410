# Task 2 Making a web client to test my server
import argparse
import socket


# Making a method to send the request to the server through the terminal with the parsed arguments from the client
def send_request(host, port, filename):
    # Create a TCP socket to establish a connection between the client and the server over the internet on a network.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl_socket:
        # Connect to the server
        cl_socket.connect((host, port))
        # Send an HTTP request to the server.
        # {filename} makes it possible for the client to write a specific file through the terminal
        request = f'GET /{filename} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        # Sending the request including the request message.
        # We encode the message since the HTTP request is a string and the socket transmits binary data.
        # sendall() sends all the data in a single transmission and blocks until all the data has been sent.
        cl_socket.sendall(request.encode())
        # receive the response
        response = cl_socket.recv(1024)
        # Decode and print the response from the server.
        print(response.decode())


def testingMultipleClients():  # Used for testing multiple clients at the same time
    host = "127.0.0.1"
    port = 8000
    filename = "index.html"

    send_request(host, port, filename)


if __name__ == '__main__':

    # Parsing arguments from the client connecting to the server.
    parser = argparse.ArgumentParser(description='HTTP client')
    parser.add_argument('host', help='server IP address or host name')
    parser.add_argument('port', type=int, help='server port')
    parser.add_argument('filename', help='path to requested object on server')
    args = parser.parse_args()

    send_request(args.host, args.port, args.filename)

# Method used for testing multiple clients
# testingMultipleClients()  # Used for testing multiple clients at the same time
