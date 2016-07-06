import socket
import pickle
import threading
import numpy
import sys
from globalvars import *
from pygame.locals import *
from constants import CAMERA_POS, ESTADO_MOTORES, DICT_MOVEMENTS
from globalvars import (
    get_camera_surface, set_camera_surface, get_sock, empty_camera_surface,
    get_clikd_btn, set_clikd_btn)


class Network():
    tcp_host = '127.0.0.1'
    tcp_port = 4004
    address = tcp_host, tcp_port

    def connect_to_server(self):
        try:
            sock = socket.create_connection(self.address, timeout=10)
            sock.settimeout(None)
            tcamera = threading.Thread(
                target=receivepic, args=('ReceivePicture', 'abc'))
            tcamera.start()
            tcinv = threading.Thread(
                target=sendpos, args=('SendPosition', 'abc'))
            tcinv.start()
        except ConnectionRefusedError:
            sock = -1
        return sock

    def disconnect_from_server(self):
        sock = get_sock()
        sock.close()

    def draw(self, screen):
        if get_sock():
            frame_surface = get_camera_surface()
            screen.blit(frame_surface, (CAMERA_POS))


def receivepic(name, abc):
    address = host, port = "127.0.0.1", 4005
    tcp_sock = socket.socket()
    tcp_sock.bind(address)
    tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
    tcp_sock.shutdown(1)
    tcp_sock.close()
    empty_camera_surface()
    print('Raspberry desconectada!')


def sendpos(name, abc):
    address = host, port = "127.0.0.1", 4006
    print("Entrou na thread...")
    try:
        tcp_sock = socket.socket()
        tcp_sock = socket.create_connection(address, timeout=10)
        tcp_sock.settimeout(None)
    except ConnectionRefusedError:
        tcp_sock = -1
    while get_sock():
        if get_clikd_btn() in ESTADO_MOTORES:
            movement = DICT_MOVEMENTS[get_clikd_btn()]
            tcp_sock.send(bytes(movement, 'UTF-8'))
            set_clikd_btn(None)
    tcp_sock.close()
