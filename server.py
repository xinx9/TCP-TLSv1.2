import socket
import ssl, sys, os

dmax = 1024

if(len(sys.argv) != 2):
    print("Usage: python3 server.py <PORT NUMBER>")
    sys.exit(1)

cert = (os.path.join(os.getcwd() + "/.cert.pem"))

if(not os.path.exists(cert)):
    os.system("openssl req -new -x509 -keyout .cert.pem -out .cert.pem -days 365 -nodes -subj '/' ")
    print("Generating Certificate")

ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.load_cert_chain(certfile='.cert.pem')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_ServerAddress = ('localhost', int(sys.argv[1]))
tcp.bind(TCP_ServerAddress)
tcp.listen(5)

while True:
    ssock, addr = tcp.accept()
    conn = ctx.wrap_socket(ssock,server_side=True) 
    data = conn.read(dmax).decode()
    print(data)
    if data:
        conn.sendall(data.encode())
    else:
        print("got nothing")
        break
conn.close()
