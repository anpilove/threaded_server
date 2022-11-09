import socket
import threading
import time


class Client:

    def __init__(self):
        self.sock = socket.socket()  # object from class socket
        self.localhost = ''
        self.port = int(input("Port to connect: "))  # port 0 to 65535
        self.run()

    def run(self):
        self.sock.connect(('', self.port))  # connect to server
        threading.Thread(target=self.recv_data).start()  # branch process
        # (first - sending connections)
        # (second - receive data from server)
        while True:
            msg = input("Message: ")
            self.sock.send(msg.encode())  # send data

    def recv_data(self):
        while True:
            data = self.sock.recv(1024).decode()  # get data
            print(data)


client1 = Client()
