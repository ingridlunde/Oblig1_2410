import http.server
import socketserver
import threading

# Task 3 - develop a multithreaded server that is capable of serving multiple requests simultaneously..

PORT = 8080  # Listens on this port
FILE_DIR = "."  # The directory to serve files from


class RequestHandler(http.server.BaseHTTPRequestHandler):

    # do_GET() "BaseHTTPRequestHandler" class in Python's http.server module, which is a default request handler
    # class for HTTP servers.It is called when an HTTP GET request is received by the server.

    # The method is responsible for handling incoming GET requests, retrieving the requested resource from the server,
    # and sending an HTTP response to the client.The method retrieves the requested resource from the server's file
    # system, creates an HTTP response message consisting of the requested file preceded by header lines, and then
    # sends the response directly to the client. If the requested file is not present on the server,
    # the method sends an HTTP "404 Not Found" message back to the client.
    def do_GET(self):  # "self" parameter is a reference to the current instance of a class. It is similar to 'this'
        print("inside do_GET")
        while True:
            # Receive the request data from the client
            request_data = self.request.recv(1024).decode("utf-8")
            print(f"Request received:")
            print(request_data)
            if not request_data:
                break

            # splits the request_data string into a list of three elements, using the space character as the separator.
            # The resulting list contains the request method, request path, and HTTP version.
            # The _ variable is assigned the third element of the list, which is the HTTP version.
            # Since the HTTP version is not used in the code snippet, we can use the _ variable to ignore it.
            print(request_method)
            request_method, request_path, _ = request_data.split(" ", 2)

            # Construct the response
            if request_method == "GET":
                print(request_method)
                # Try to open the requested file
                try:
                    with open(request_data[1:], "rb") as f:
                        file_content = f.read()

                    # Send a 200 OK response to the header
                    # 200 request means that the request has succeeded and the server has returned the requested
                    # data. The response body typically contains the data that was requested by the client.
                    # sends the initial line of the HTTP response, including the HTTP status # code
                    self.send_response(200)
                    # Sends HTTP headers, which provide additional information about the response.
                    # Headers are sent as key-value pairs, with the header name as the key and the header value as
                    # value send an HTTP header indication the response body is HTML
                    self.send_header("Content-type", "text/html")

                    # Method call that adds an HTTP header to the response
                    # The Content-length header indicates the size of the response body in bytes.
                    # len(file_content) is the length of the file content in bytes, which is calculated using the
                    # built-in len() function in Python
                    self.send_header("Content-length", len(file_content))

                    # Signals the end of the headers section of the HTTP response.
                    self.end_headers()
                    # Send file content
                    # The wfile attribute is a file-like object that allows you to send data to the client.
                    self.wfile.write(file_content)

                # IOE error: Not found
                except FileNotFoundError:
                    # Send 404 response
                    self.send_error(404, "File not found")
            else:
                # Sends error if the client dont implement a file.
                self.send_error(501, "Not implemented")


# Creates a threaded TCP server object that listens for incoming connections on the specific port.
# Threaded server takes two arguments.
# The server listens on a spesific port and will set up the TCP connection through another port and service the client
# in a sperated thread.

# The ThreadingMixIn class provides the behavior necessary for a single-threaded TCP server to handle multiple requests
# simultaneously by creating a new thread for each incoming connection.

# The TCPServer class provides the basic infrastructure for a TCP server by listening for incoming connections on a
# specified host and port, and then creating a new socket for each incoming connection.
"""class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):"
    "# The pass statement in the class definition is simply a placeholder that indicates there are no additional"
    "# attributes or methods defined in the class. "
    "pass"""

""""
if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("", PORT), RequestHandler)
    # Creates a TCP server object that listens for incoming connections on the specific port.
    # TCP server takes two arguments.
    # The server adress(which is represented as a tuple, with the hostname or IP adress and port number).
    # The handler class, which is used to handle incoming request. Myhandler is the class
    with server:
        print(f"server listening at port {PORT} - test")

        # Start a new thread to handle each request.
        # Creates a new thread that will call the method serve_forever() method which starts the server and keeps it
        # looping for incoming request. By calling the method of the 'TcpSrver' class in a seperate thread, the server
        # can listen for incoming connections and handle multiple requests simultaneously while the main thread
        # continues to run.
        # it is prosessed by the request handler class and a response is sent back to the client.
        server_thread = threading.Thread(target=server.serve_forever)

        # Thread.daemon means that the new thread will be a daemon thread, and will be terminated automatically when the
        # main program exits. This can be useful in situations where you want to start a new thread for a short-lived
        # task that does not need to complete before the program finishes execution.
        server_thread.daemon = True
        # Thread.start() will start the new thread and execute the target function in the background while the main
        # thread continues running.
        server_thread.start()

        # Wait for user input to stop the server.
        input("Press any key to stop the server...\n") """

if __name__ == "__main__":
    with socketserver.TCPServer(("", 8080), RequestHandler) as httpd:
        print("Serving at port 8080")
        httpd.serve_forever()
