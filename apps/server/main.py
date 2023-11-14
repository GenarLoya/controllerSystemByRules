import http.server
import socketserver
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

PORT = int(os.getenv("PORT", 8000))  # Get PORT from environment variable or use default value

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
