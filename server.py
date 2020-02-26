import http.server
import socketserver

PORT = 8890
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("Server is running at ", PORT)
    Print ("To test from dockerized version, please run http://loaclhost:<exposed port>")
    httpd.serve_forever()
