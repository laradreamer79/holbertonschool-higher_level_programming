#!/usr/bin/python3
"""
Task 03 - Simple API using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Simple API handler."""

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            body = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


def run():
    server = HTTPServer(("0.0.0.0", 8000), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()

