import socket
import ssl, sys, os
dmax = 1024
os.system("openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes -subj '/' ")
ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.load_cert_chain(certfile='./server.pem')
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_ServerAddress = ('localhost', int(sys.argv[1]))
tcp.bind(TCP_ServerAddress)
tcp.listen(5)
while True:
    ssock, addr = tcp.accept()
    conn = ctx.wrap_socket(ssock,server_side=True)
    while True:
        #data = conn.recv(dmax)
        data = conn.read(dmax)
        print(data)
        if data:
            conn.sendall(data)
        else:
            print("got nothing")
            break
        conn.close()