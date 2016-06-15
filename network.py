import socket
from globalvars import *

class Network():
    address = host, port = '127.0.0.1', 4004

    def connect_to_server(self):
        try:
            sock = socket.create_connection(self.address, timeout=10)
            sock.settimeout(None)
        except ConnectionRefusedError:
            sock = -1
        return sock

    def disconnect_from_server(self):
        sock = get_sock()
        sock.close()
