from http.server import HTTPServer
from .handlers import RequestHandler
from .validation import validate_openapi_spec


class SimpleHTTPServer:
    """
    class to initiate http servers
    """

    def __init__(self, host, port=5000) -> None:
        """
        Initialize the server with the host and port.
        """
        self.host = host
        self.port = port
        self.server = None

    def start_server(self):
        self.server = HTTPServer((self.host, self.port), RequestHandler)
        try:
            validate_openapi_spec("/home/yassine/yassine/Pyth_playground/api/spec.yml")
            print(f"Starting server on {self.host}:{self.port}")
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
