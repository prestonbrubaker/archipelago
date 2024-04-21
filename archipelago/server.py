import socket
import logging
import threading

def tcp_server():
    host = '0.0.0.0'
    port = 5001
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on port {port}")
    logging.info(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        try:
            with conn:
                file_data = bytearray()
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file_data.extend(data)
                
                with open('organism_in.txt', 'wb') as f:
                    f.write(file_data)
                print("File received and saved as organism_in.txt")
        except Exception as e:
            print(f"Error handling connection from {addr}: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    tcp_server()