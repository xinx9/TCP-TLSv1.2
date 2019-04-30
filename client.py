import socket
import ssl, sys, os
dmax = 1024
if(len(sys.argv) != 2):
    print("Usage: python3 client.py <PORT NUMBER>")
    sys.exit(1)
TCP_ServerAddress = ('localhost', int(sys.argv[1]))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
conn = ctx.wrap_socket(sock, server_side=False, server_hostname='localhost')

try:
    conn.connect(TCP_ServerAddress)
    message = input(">")
    conn.sendall(message.encode())
    data = conn.read(dmax).decode()
    print(data)
finally:
    conn.close()
