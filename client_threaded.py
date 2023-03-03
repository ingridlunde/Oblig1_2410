# Task 2 Making a web client to test my server. There are some changes to the code since it is suppose to be used
# on a multithreaded server
import argparse
import socket

HOST = 'localhost'  # Testing from the same computer. Then I can use 'localhost' or 127.0.0.1
PORT = 8080  # Servers port number


# Making a method to send the request to the server through the terminal with the parsed arguments from the client
def send_request(host, port, filename):
    print("inside send_request")
    # Create a TCP socket to establish a connection between the client and the server over the internet og a network.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl_socket:
        # Connect to the server
        cl_socket.connect((host, port))
        print("You are connected to Inga's server")
        # Send an HTTP request to the server.
        # {filename} makes it possible for the client to write a specific file through the terminal
        request = f'GET /{filename} HTTP/1.1\r\nHost: {host}\r\n\r\n'
        # Sending the request including the request message.
        # We encode the message since the HTTP request is a string and the socket transmits binary data.
        # sendall() sends all the data in a single transmission and blocks until all the data has been sent.
        cl_socket.sendall(request.encode())
        # Receive the response from the server

        response = b''
        while True:
            data = cl_socket.recv(1024)
            if not data:
                break
            response += data

        # Decode the response data and print it
        print("Printing the response")
        print(response.decode('utf-8'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HTTP client')
    parser.add_argument('host', help='server IP address or host name')
    parser.add_argument('port', type=int, help='server port')
    parser.add_argument('filename', help='path to requested object on server')
    args = parser.parse_args()

    send_request(args.host, args.port, args.filename)
