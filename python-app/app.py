import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class JSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        data = {
            "status": "success",
            "message": "Bienvenue sur ma mini-application Python conteneurisée !",
            "version": "1.0"
        }
        self.wfile.write(json.dumps(data).encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), JSONHandler)
    print("Serveur HTTP en écoute sur le port 5000...")
    server.serve_forever()
