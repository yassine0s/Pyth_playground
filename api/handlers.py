from http.server import BaseHTTPRequestHandler
import json

import logging


class RequestHandler(BaseHTTPRequestHandler):
    "request handler"

    def do_GET(self):
        logging.info("Received a GET request")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        response = {"message": "Get response"}
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        logging.info("Received a POST request")
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "You sent: {}".format(post_data.decode("utf-8"))}
        self.wfile.write(json.dumps(response).encode("utf-8"))
