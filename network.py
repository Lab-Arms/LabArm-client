import socket
import pickle
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
    print("Camera pronta pra envio...")
    conn, addr = tcp_sock.accept()
    print("Raspberry conectada...")
    while conn and get_sock():
        chunk = bytes()
        conn.send(bytes('ready', 'UTF-8'))
        size = conn.recv(1024)
        size = int(size.decode('UTF-8'))
        conn.send(bytes(str(size), 'UTF-8'))
        while sys.getsizeof(chunk) < size:
            chunk += conn.recv(46080)
        frame = pickle.loads(chunk)
        frame = numpy.rot90(frame, 1)
        surface = pygame.surfarray.make_surface(frame)
        set_camera_surface(surface)
    conn.close()
    tcp_sock.close()
    print('Raspberry desconectada!')
