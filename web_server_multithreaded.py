import http.server
import socketserver
import threading

# Task 3 - develop a multithreaded server that is capable of serving multiple requests simultaneously..

PORT = 8000  # Listens on this port
FILE_DIR = "."  # The directory to serve files from


# Handler class which takes the handler in as an argument
# A Handler function handles a respons to a specific request and provides a way to serv files and content over the web
# SimpleHTTPRequestHandler provides a basic implementation og an HTTP server that can
# serve files from a local directory.
class MyHandler(http.server.SimpleHTTPRequestHandler):

    # do_GET() "BaseHTTPRequestHandler" class in Python's http.server module, which is a default request handler
    # class for HTTP servers.It is called when an HTTP GET request is received by the server.

    # The method is responsible for handling incoming GET requests, retrieving the requested resource from the server,
    # and sending an HTTP response to the client.The method retrieves the requested resource from the server's file
    # system, creates an HTTP response message consisting of the requested file preceded by header lines, and then
    # sends the response directly to the client. If the requested file is not present on the server,
    # the method sends an HTTP "404 Not Found" message back to the client.
    def do_GET(self):  # "self" parameter is a reference to the current instance of a class. It is similar to 'this'
        # Parse the request after a spesific file_path. If there is no file_path. index.html is sent
        file_path = self.path[1:]  # Remove leading slash

        # If not file in path, the index.hmtl would be sent by default.
        if not file_path:
            file_path = "index.html"  # Serve index.html by default

        # Try to open the requested file
        try:
            f = open(FILE_DIR + "/" + file_path, "rb")
            file_content = f.read()
            f.close()

            # Send a 200 OK response to the header
            # 200 request means that the request has succeeded and the server has returned the requested data.
            # The response body typically contains the data that was requested by the client.
            self.send_response(200)  # sends the initial line of the HTTP response, including the HTTP status code

            # Sends HTTP headers, which provide additional information about the response.
            # Headers are sent as key-value pairs, with the header name as the key and the header value as the value
            self.send_header("Content-type", "text/html")  # send an HTTP header indication the response body is HTML

            # Method call that adds an HTTP header to the response
            # The Content-length header indicates the size of the response body in bytes.
            # len(file_content) is the length of the file content in bytes, which is calculated using the built-in
            # len() function in Python
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


# Creates a threaded TCP server object that listens for incoming connections on the specific port.
# Threaded server takes two arguments.
# The server listens on a spesific port and will set up the TCP connection through another port and service the client
# in a sperated thread.

# The ThreadingMixIn class provides the behavior necessary for a single-threaded TCP server to handle multiple requests
# simultaneously by creating a new thread for each incoming connection.

# The TCPServer class provides the basic infrastructure for a TCP server by listening for incoming connections on a
# specified host and port, and then creating a new socket for each incoming connection.
class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # The pass statement in the class definition is simply a placeholder that indicates there are no additional
    # attributes or methods defined in the class.
    pass


# Creates a TCP server object that listens for incoming connections on the specific port.
# TCP server takes two arguments.
# The server adress(which is represented as a tuple, with the hostname or IP adress and port number).
# The handler class, which is used to handle incoming request. Myhandler is the class
with ThreadedHTTPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)

    # Start a new thread to handle each request.
    # Creates a new thread that will call the method serve_forever() method which starts the server and keeps it
    # looping for incoming request. By calling the method of the 'TcpSrver' class in a seperate thread, the server can
    # listen for incoming connections and handle multiple requests simultaneously while the main thread continues to
    # run.
    # it is prosessed by the request handler class and a response is sent back to the client.
    thread = threading.Thread(target=httpd.serve_forever)

    # Thread.daemon means that the new thread will be a daemon thread, and will be terminated automatically when the
    # main program exits. This can be useful in situations where you want to start a new thread for a short-lived task
    # that does not need to complete before the program finishes execution.
    thread.daemon = True
    # Thread.start() will start the new thread and execute the target function in the background while the main thread
    # continues running.
    thread.start()

    # Wait for user input to stop the server.
    input("Press any key to stop the server...\n")
    # Shut down the server
    httpd.shutdown()
    # a method which starts the server and keeps it looping for incoming request. As soon as a requesr arrives,
    # it is prosessed by the request handler class and a response is sent back to the client.
    httpd.serve_forever()
