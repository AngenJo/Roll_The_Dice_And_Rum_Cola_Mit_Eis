import socket
import sys

MAX_USERS  = 30

# USERS
class User:
    name = "Player"
    sock = None


    def __init__(self):
        print("const")
    
    def connect(self, server_address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('connecting to %s port %s' % server_address)
        self.sock.connect(server_address)