import http.server
import socketserver
import os
import pathlib

# Port configuration
PORT = 8000

# Change working directory to the script's location (project root)
project_root = pathlib.Path(__file__).parent.resolve()
os.chdir(project_root)

# Define request handler that serves files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT} (http://localhost:{PORT}/) ...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()
