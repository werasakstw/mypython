from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('Hello! how do you do?'.encode())

    def do_POST(self):
        # Read body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        # Create response
        res = BytesIO()
        res.write(b'Received: ')
        res.write(body)

        # Send response
        self.send_response(200)
        self.end_headers()
        self.wfile.write(res.getvalue())

HTTPServer(('127.0.0.1', 8080), MyHandler).serve_forever()

# curl 127.0.0.1:8080
# curl 127.0.0.1:8080 -X POST -d Hello
