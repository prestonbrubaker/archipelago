import socket
import connections

def client(server_host, server_port, world_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        s.sendall(world_id.encode())  # Send world ID upon connection

def send_file(conn, receiver_id, file_content):
    message = f"{receiver_id}\n{file_content}"
    if receiver_id in connections:
        connections[receiver_id].sendall(message.encode())

def handle_client(conn, addr):
    world_id = None
    while True:
        data = conn.recv(1024)
        if not data:
            break
        if world_id is None:
            world_id = data.decode().strip()
            connections[world_id] = conn
        else:
            # Assuming the data format is 'receiver_id\nfile_content'
            receiver_id, file_content = data.decode().split('\n', 1)
            send_file(conn, receiver_id, file_content)
    conn.close()
