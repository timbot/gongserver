
import http.server
import socketserver
import argparse
import subprocess

class GongHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Gong!\n")

        print("Received request. Playing sound.")
        try:
            cmd = ["mpg123"]
            if self.server.mono:
                cmd.append("-m")
            cmd.append(self.server.sound_file)
            subprocess.Popen(cmd)
        except FileNotFoundError:
            print("mpg123 not found. Please install it.")
        except Exception as e:
            print(f"Error starting sound process: {e}")

def main():
    parser = argparse.ArgumentParser(description="A simple webserver that plays a sound on request.")
    parser.add_argument("--sound-file", required=True, help="Path to the sound file to play.")
    parser.add_argument("--port", type=int, default=8000, help="Port to listen on.")
    parser.add_argument("--mono", action="store_true", help="Force mono output.")
    args = parser.parse_args()

    Handler = GongHandler
    httpd = socketserver.TCPServer(("", args.port), Handler)
    httpd.allow_reuse_address = True
    httpd.sound_file = args.sound_file
    httpd.mono = args.mono

    print(f"Serving at port {args.port}")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
