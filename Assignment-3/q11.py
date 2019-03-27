import socket
def server():
    count = 0
    host = "localhost"
    port = 12345
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        while True:
            request = c.recv(4096)
            count += 1
            data = "Hello from server"
            http_response = "HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n"+"<html><body>"+data+"</body></html>\n"
            c.sendall(http_response.encode('ascii'))
            c.close()
            break
    s.close()
if __name__ == '__main__':
    server()
