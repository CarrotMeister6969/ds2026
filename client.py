import socket
import os

SERVER_IP = "127.0.0.1"
PORT = 5000

file_path = input("Enter file path to send: ")

if not os.path.exists(file_path):
    print("File not found.")
    quit()

file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

client.send(file_name.encode())
client.recv(2)  

client.send(str(file_size).encode())
client.recv(2)  

with open(file_path, "rb") as f:
    while True:
        data = f.read(4096)
        if not data:
            break
        client.send(data)

print("File sent successfully!")
client.close()