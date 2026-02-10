#!/usr/bin/python3
"""
Task 03 - Simple API using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


HOST = "0.0.0.0"
PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for a simple API."""

    def _send_text(self, status_code, text):
        """Send a plain text response."""
        body = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status_code, payload):
        """Send a JSON response."""
        body_str = json.dumps(payload)
        body = body_str.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
            return

        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, data)
            return

        if self.path == "/status":
            self._send_text(200, "OK")
            return

        # Optional endpoint (mentioned in expected output)
        if self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json(200, info)
            return

        self._send_text(404, "Endpoint not found")


def run_server():
    """Start the HTTP server."""
    server = HTTPServer((HOST, PORT), SimpleAPIHandler)
    print(f"Server running on http://localhost:{PORT}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

