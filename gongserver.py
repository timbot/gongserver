
import http.server
import socketserver
import argparse
import subprocess

class GongHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print("Received request. Playing sound.")
        try:
            subprocess.run(["mpg123", self.server.sound_file], check=True)
        except FileNotFoundError:
            print("mpg123 not found. Please install it.")
        except subprocess.CalledProcessError as e:
            print(f"Error playing sound: {e}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Gong!\n")

def main():
    parser = argparse.ArgumentParser(description="A simple webserver that plays a sound on request.")
    parser.add_argument("--sound-file", required=True, help="Path to the sound file to play.")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on.")
    args = parser.parse_args()

    Handler = GongHandler
    httpd = socketserver.TCPServer(("", args.port), Handler)
    httpd.allow_reuse_address = True
    httpd.sound_file = args.sound_file

    print(f"Serving at port {args.port}")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
