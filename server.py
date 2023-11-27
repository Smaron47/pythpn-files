
import socket

BUFFER=2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0',8888))
s.listen()
conn, addr = s.accept()
print(f'Connected to the {addr}')
while True:
    data = conn.recv(BUFFER)
    if not data:
        break
    conn.sendall(data)
