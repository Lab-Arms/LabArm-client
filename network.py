import socket
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
        except ConnectionRefusedError:
            sock = -1
        return sock

    def disconnect_from_server(self):
        sock = get_sock()
        sock.close()

    def receivepic(self):
        return frame_surface

    def draw(self, screen):
        if get_sock():
            frame_surface = get_camera_surface()
            screen.blit(frame_surface, (CAMERA_RECT_X, CAMERA_RECT_Y))
