import http.server
from prometheus_client import start_http_server, Counter

REQUESTS = Counter('welcome_request_total', 'Total GET requests for welcome page test server')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Welcome Satheesh")
        

if __name__ == "__main__":
    start_http_server(7001)
    server = http.server.HTTPServer(('192.168.0.126', 7000), MyHandler)
    server.serve_forever()
    
    