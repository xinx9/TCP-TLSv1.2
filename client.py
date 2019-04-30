import socket
import ssl, sys, os
dmax = 1024
TCP_ServerAddress = ('localhost', int(sys.argv[1]))
print(TCP_ServerAddress)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
conn = ctx.wrap_socket(sock, server_side=False, server_hostname='localhost')
try:
    conn.connect(TCP_ServerAddress)
    message = "ssl test"
    conn.sendall(message)
    data = conn.recv(dmax)
    print(len(data))
    print("\n")
    print(data)
finally:
    conn.close()