# https://realpython.com/python-sockets/
# check out the **socketserver** standard module, too

import socket

HOST = "127.0.0.1"
PORT = 22222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)

print("Disconnected")
print("Bye!")
