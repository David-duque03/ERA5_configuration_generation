#!/usr/bin/env python3
"""
Simple HTTP Server for CONFIG.conf Generator Web Application
Launches a local web server to serve the application files.
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

# Configuration
PORT = 8080
HOST = "0.0.0.0"  # Listen on all network interfaces

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to add CORS headers and handle file types"""
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        """Override to customize log messages"""
        print(f"[{self.log_date_time_string()}] {format % args}")

def get_local_ip():
    """Get the local IP address"""
    import socket
    try:
        # Create a socket to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "localhost"

def main():
    """Start the web server"""
    # Change to the script directory
    web_dir = Path(__file__).parent
    os.chdir(web_dir)
    
    local_ip = get_local_ip()
    
    print("=" * 70)
    print("🌍 CONFIG.conf Generator - Servidor Web")
    print("=" * 70)
    print(f"\n📁 Directorio: {web_dir}")
    print(f"\n🌐 URLs de acceso:")
    print(f"   • Local:  http://localhost:{PORT}")
    print(f"   • Red:    http://{local_ip}:{PORT}")
    print(f"\n✨ Abriendo navegador automáticamente...")
    print(f"\n⚠️  Para detener el servidor: Ctrl+C")
    print("=" * 70)
    print()
    
    # Create server
    with socketserver.TCPServer((HOST, PORT), MyHTTPRequestHandler) as httpd:
        # Open browser automatically
        webbrowser.open(f"http://{HOST}:{PORT}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n" + "=" * 70)
            print("🛑 Servidor detenido correctamente")
            print("=" * 70)
            httpd.shutdown()

if __name__ == "__main__":
    main()
