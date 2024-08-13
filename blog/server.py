from http.server import HTTPServer, SimpleHTTPRequestHandler

port = 10000
server_address = ('0.0.0.0', port)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f'Serving on port {port}...')
httpd.serve_forever()
