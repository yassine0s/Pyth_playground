from http.server import HTTPServer, SimpleHTTPRequestHandler
from handlers import RequestHandler
from validation import validate_openapi_spec

class SimpleHTTPServer:
    def __init__(self, host, port=8080, handler="DefaultHandler") -> None:
        """
        Initialize the server with the host and port.
        """
        self.host = host
        self.port = port
        self.handler = handler
        self.server = None

    def start_server(self):
        self.server = HTTPServer(self.host, self.port, self.handler)
        try:
            validate_openapi_spec("./spec.yml")
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
            self.close_server()

    def close_server(self):
        """
        Stop the HTTP server.
        """
        if self.server:
            self.server.server_close()
            print("Server closed.")