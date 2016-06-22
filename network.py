import socket
from globalvars import *
from canvas import Canvas
import pygame
from pygame.locals import *
import threading
import numpy
import cv2


class Network():
    host = '127.0.0.1'
    port = 4004
    address = (host, port)

    def connect_to_server(self):
        try:
            sock = socket.create_connection(self.address, timeout=10)
            sock.settimeout(None)
            t = threading.Thread(target=receivepic, args=('def', self.address))
            t.start()
        except ConnectionRefusedError:
            sock = -1
        return sock

    def disconnect_from_server(self):
        sock = get_sock()
        sock.close()

    # def connect_udp_server(self, nothing, address):
    #     sock = get_sock
    #     if(get_sock):
    #         udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #         udpsock.bind((self.udpaddress))
        
    #         frame,udpaddress = udpsock.recvfrom(4096)
    #         cam = frame.formstring()
    #         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         nf = pygame.surfarray.make_surface(np.transpose(rgb_frame, (1,0,2)))
    #         screen.blit(nf, (0,0))
    #         pygame.display.flip()

    #     return udpsock


def receivepic(nothing, address):
    udphost = address[0]
    udpport = address[1] + 1
    udpclient = (udphost, udpport + 1)
    
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsock.bind(udpclient)
    connected = True
    data, udpserver = s.recvfrom(1024)

    if data == 'conectado':
        udpsock.sendto('eh nois', addr)
    while connected:
        import ipdb; ipdb.set_trace()
