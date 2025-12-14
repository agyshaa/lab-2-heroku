import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = int(os.environ.get("PORT", 5000))

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Heroku! Lab work by Vika.</h1>")

httpd = HTTPServer(('0.0.0.0', port), MyHandler)
print(f"Server running on port {port}")
httpd.serve_forever()