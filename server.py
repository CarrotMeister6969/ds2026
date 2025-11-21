import socket
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")
print(f"Files will be saved this folder: {BASE_DIR}")

conn, addr = server.accept()
print("Connected by", addr)

file_name = conn.recv(1024).decode().strip()
file_name = os.path.basename(file_name) 
print("Receiving file:", file_name)

conn.send(b"OK")

file_size = int(conn.recv(1024).decode().strip())
print("File size:", file_size, "bytes")

conn.send(b"OK")

save_path = os.path.join(BASE_DIR, "received_" + file_name)

received = 0
with open(save_path, "wb") as f:
    while received < file_size:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)
        received += len(data)

print(f"\nTransfer Completed")
print(f"File saved at: {save_path}")

conn.close()
server.close()