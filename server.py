import socket
import threading
import time


class Server:
    def __init__(self):
        self.clients = []
        self.sock = socket.socket()  # object from class socket
        self.localhost = ''  # host name
        self.port = int(input("Port: "))  # port 0 to 65535
        self.run()


    def run(self):
        self.sock.bind(('', self.port))  # creating sever
        self.sock.listen(5)  # listen to 5 clients
        while True:
            conn, addr = self.sock.accept()  # accepting connection from clients in while
            self.clients.append(conn)
            threading.Thread(target=self.data_client, args=[conn, addr]).start()
            # branch process (first - accepting connections)
            # (second - receive data in data_clients)

    def data_client(self, conn, addr):
        while True:
            data = conn.recv(1024).decode()
            # conn.send("Message delivered".encode())
            print(f"Message from {addr[0]} is {data}")
            if not data:
                break
            for sock in self.clients:
                if sock != conn:
                    sock.send(f"Message from {addr[0]} is {data}".encode())

        conn.close()


server = Server()
