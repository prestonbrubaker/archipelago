import socket

def send_file(server_ip, server_port, file_path):
    """Send a file to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, server_port))
        local_ip = sock.getsockname()[0]  # Get local IP connected to the server
        sock.sendall(f"{local_ip}\n".encode())
        with open(file_path, "rb") as f:
            while True:
                bytes_read = f.read(1024)
                if not bytes_read:
                    break
                sock.sendall(bytes_read)
        print(f"File {file_path} sent to {server_ip}:{server_port}")

def receive_file(server_ip, server_port, destination_file):
    """Receive a file from the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((server_ip, server_port))
        with open(destination_file, 'wb') as f:
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                f.write(data)
        print(f"Received file saved as {destination_file}")

if __name__ == "__main__":
    server_ip = '73.166.159.150'
    server_port = 5000
    file_to_send = 'organism_out.txt'
    file_to_receive = 'organism_in.txt'
    
    # Send a file to the server
    send_file(server_ip, server_port, file_to_send)
    
    # Optionally receive a file from the server
    receive_file(server_ip, server_port, file_to_receive)
