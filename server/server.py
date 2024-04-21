import socket
import threading
import logging

connections = {}

def handle_client(conn, addr):
    try:
        with open("received_file", "wb") as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                world_id = data.decode().strip()
                connections[world_id] = conn
                f.write(data)
        forward_file("received_file", addr)
    except Exception as e:
        logging.error(f"Error handling client {addr}: {e}...        oops :(")
    finally:
        conn.close()
        if world_id in connections:
            del connections[world_id]

def forward_file(file_path, addr):
    destination_ip = 'destination_device_ip'
    destination_port = 5001
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((destination_ip, destination_port))
        with open(file_path, "rb") as f:
            while True:
                bytes_read = f.read(1024)
                if not bytes_read:
                    break
                sock.sendall(bytes_read)


def server():
    host = '0.0.0.0'
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    logging.info(f"Server listening on {host}:{port}!")

    try:
        while True:
            try:
                conn, addr = server_socket.accept()
                threading.Thread(target=handle_client, args=(conn, addr)).start()
            except Exception as e:
                logging.error(f"Error accepting connections: {e}")
    except KeyboardInterrupt:
        logging.info("Server is shutting down...")
    finally:
        server_socket.close()
        logging.info("Server socket closed!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    server()
