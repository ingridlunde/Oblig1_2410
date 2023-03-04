import socket
import threading
import sys

# Task 3 - develop a multithreaded server that is capable of serving multiple requests simultaneously..

FILE_DIR = "."  # The directory to serve files from


# Handler def which takes the handler in as an argument
# A Handler function handles a respons to a specific request and provides a way to serv files and content over the web
# serve files from a local directory.
def handle_client(conn):
    """Handle a client request"""
    # Receive the request data from the client
    request = conn.recv(1024)
    print(f"Request received:")

    # Assume that the request is a GET request
    filename = request.split()[1].decode()
    print(filename)
    try:
        # Open the requested file
        with open(FILE_DIR + "/" + filename, "rb") as f:
            print(filename)
            content = f.read()
            # Send a 200 OK response to the header
            # 200 request means that the request has succeeded and the server has returned the requested
            # data. The response body typically contains the data that was requested by the client.
            # sends the initial line of the HTTP response, including the HTTP status # code
            conn.sendall(b'HTTP/1.0 200 OK\r\n\r\n' + content)
    # IOE error: Not found
    except FileNotFoundError:
        # If the file is not found, return a 404 error
        conn.sendall(b'HTTP/1.0 404 Not Found\r\n\r\nFile not found')

    # Close the connection
    conn.close()


def run_server(port):
    """Run the multithreaded server."""
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set the socket to reuse the address
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the specified port
    server_socket.bind(('localhost', port))
    # Listen for incoming connections
    # The server listens on a spesific port and will set up the TCP connection through another port
    # and service the client
    server_socket.listen(5)
    print(f'Server listening on port {port}')

    while True:
        # Accept a new client connection
        conn, addr = server_socket.accept()
        print(f'Client connected: {addr}')

        # Start a new thread to handle the client request
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()


if __name__ == '__main__':
    # Parse the command line arguments
    port = 8000
    # Run the server
    run_server(port)
