import socket
import threading
import time


class Client:

    def __init__(self):
        self.sock = socket.socket()  # создаем сокет из класса сокет
        self.localhost = ''
        self.port = int(input("Port to connect: "))  # port 0 до 65535
        self.run()

    def run(self):
        self.sock.connect(('', self.port))
        threading.Thread(target=self.recv_data).start()
        while True:
            msg = input("Message: ")
            self.sock.send(msg.encode())

    def recv_data(self):
        while True:
            data = self.sock.recv(1024).decode()
            print(data)


client1 = Client()
