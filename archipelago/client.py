import socket
import time

def send_file(target_ip, port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, port))
    print("Connected to server")

    file_content = ""

    while file_content.strip() == "[]" or file_content.strip() == "":
        try:
            with open(file_path, 'r') as file:
                file_content = file.read().strip()
            if file_content == "[]" or file_content == "":
                print("File content not ready, waiting...")
                time.sleep(5)
        except FileNotFoundError:
            print("File not found, waiting for file to be updated...")
            time.sleep(5) 

    with open(file_path, 'rb') as file:
        client_socket.sendall(file.read())

    print("File sent")

if __name__ == "__main__":
    target_ip = '192.168.1.31'  # Replace this with the actual server IP address
    port = 5001
    send_file(target_ip, port, 'organism_out.txt')
