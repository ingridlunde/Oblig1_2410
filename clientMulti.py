import socket
import sys


def send_request(host, port, filename):
    """Send a GET request to the server."""
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((host, port))
    # Send the GET request
    request = f'GET /{filename} HTTP/1.0\r\n\r\n'.encode()
    print(request)
    client_socket.send(request)

    # Receive the response from the server
    response = client_socket.recv(1024)
    print(response.decode())

    # Close the connection
    client_socket.close()


if __name__ == '__main__':
    # Parse the command line arguments
    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    # Send the GET request to the server
    print(filename)
    print(host)
    print(port)
    send_request(host, port, filename)
