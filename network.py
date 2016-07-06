import socket
import pickle
import threading
import numpy
import sys
from globalvars import *
from pygame.locals import *
from constants import CAMERA_POS, ESTADO_MOTORES, DICT_MOVEMENTS
from globalvars import (
    get_camera_surface, set_camera_surface, get_possock, get_camsock,
    set_possock, set_camsock, empty_camera_surface, get_clikd_btn,
    set_clikd_btn)


class Network():
    tcp_host = '127.0.0.1'
    tcp_port = 4004
    address = tcp_host, tcp_port

    def connect_to_server(self):
        tcamera = threading.Thread(
            target=receivepic, args=('ReceivePicture', 'abc'))
        tcamera.start()
        tcinv = threading.Thread(
            target=sendpos, args=('SendPosition', 'abc'))
        tcinv.start()

    def disconnect_from_server(self):
        camsock = get_camsock()
        possock = get_possock()
        set_camsock(camsock.close())
        set_possock(possock.close())

    def draw(self, screen):
        if get_possock() or get_camsock():
            frame_surface = get_camera_surface()
            screen.blit(frame_surface, (CAMERA_POS))


def receivepic(name, abc):
    address = host, port = "127.0.0.1", 4005
    try:
        tcp_sock = socket.socket()
        tcp_sock = socket.create_connection(address, timeout=10)
        tcp_sock.settimeout(None)
        set_camsock(tcp_sock)
    except ConnectionRefusedError:
        tcp_sock = -1
    print("Conectado na Raspberry...")
    while get_camsock():
        pass
    empty_camera_surface()
    print('Raspberry desconectada!')

    #     chunk = bytes()
    #     tcp_sock.send(bytes('ready', 'UTF-8'))
    #     size = tcp_sock.recv(1024)
    #     size = int(size.decode('UTF-8'))
    #     tcp_sock.send(bytes(str(size), 'UTF-8'))
    #     while sys.getsizeof(chunk) < size:
    #         chunk += tcp_sock.recv(46080)
    #     frame = pickle.loads(chunk)
    #     frame = numpy.rot90(frame, 1)
    #     surface = pygame.surfarray.make_surface(frame)
    #     set_camera_surface(surface)


def sendpos(name, abc):
    address = host, port = "127.0.0.1", 4006
    try:
        tcp_sock = socket.socket()
        tcp_sock = socket.create_connection(address, timeout=10)
        tcp_sock.settimeout(None)
        set_possock(tcp_sock)
    except ConnectionRefusedError:
        tcp_sock = -1
    print("Pronto para enviar movimento...")
    while get_possock():
        if get_clikd_btn() in ESTADO_MOTORES:
            movement = DICT_MOVEMENTS[get_clikd_btn()]
            tcp_sock.send(bytes(movement, 'UTF-8'))
            set_clikd_btn(None)
