import socket
import threading
import numpy
import sys
from globalvars import *
from pygame.locals import *
from constants import CAMERA_RECT_X, CAMERA_RECT_Y
from globalvars import get_camera_surface, set_camera_surface, get_sock


class Network():
    tcp_host = '127.0.0.1'
    tcp_port = 4004
    address = tcp_host, tcp_port

    def connect_to_server(self):
        try:
            sock = socket.create_connection(self.address, timeout=10)
            sock.settimeout(None)
            t = threading.Thread(
                target=receivepic, args=('ReceivePicture', 'abc'))
            t.start()
        except ConnectionRefusedError:
            sock = -1
        return sock

    def disconnect_from_server(self):
        sock = get_sock()
        sock.close()

    def draw(self, screen):
        if get_sock():
            frame_surface = get_camera_surface()
            screen.blit(frame_surface, (CAMERA_RECT_X, CAMERA_RECT_Y))


def receivepic(name, abc):
    address = host, port = "127.0.0.1", 4005
    tcp_sock = socket.socket()
    tcp_sock.bind(address)
    tcp_sock.listen(5)
    print("CAMERA PRONTA PRA ENVIO...\n")
    while True:
        conn, addr = tcp_sock.accept()
        print("RASP CONECTADA...\n")
        while conn:
            size = conn.recv(1024)
            size = int(size.decode('UTF-8'))
            temp = ''
            conn.send(bytes('ok', 'UTF-8'))
            while sys.getsizeof(temp) <= size:
                data = conn.recv(46080)
                temp += str(data)

            frame = numpy.fromstring(temp, dtype=numpy.uint8)
            frame = frame.reshape(640, 480, 3)
            surface = pygame.surfarray.make_surface(frame)
            set_camera_surface(surface)
    conn.close()
    tcp_sock.close()
