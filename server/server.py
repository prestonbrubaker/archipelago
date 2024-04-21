import socket
import threading

connections = {}  # Dictionary to map world IDs to connections

def handle_client(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        world_id = data.decode().strip()
        connections[world_id] = conn  # Store connection associated with world ID
    conn.close()

def server():
    host = '0.0.0.0'
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            # Handle each client connection in a new thread (or use asyncio)
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    finally:
        server_socket.close()
