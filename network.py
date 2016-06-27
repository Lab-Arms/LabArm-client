import socket
from globalvars import *
from canvas import Canvas
import pygame
from pygame.locals import *
import threading
import numpy
import cv2
from constants import CAMERA_RECT_X, CAMERA_RECT_Y


class Network():
    host = '127.0.0.1'
    port = 4004
    address = (host, port)

    def connect_to_server(self, screen):
        try:
            sock = socket.create_connection(self.address, timeout=10)
            sock.settimeout(None)
            t = threading.Thread(target=receivepic, args=('def', self.address, screen))
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


def receivepic(nothing, address, screen):
    host = '127.0.0.1'
    udp_port = 5005
    udp_address = host, udp_port
    # udphost = address[0]
    # udpport = address[1] + 1
    # udpclient = (udphost, udpport + 1)
    # udpserver = (udphost, udpport)
    
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpsock.bind(udp_address)

    temp=""

    while(True):
        data,addr = udpsock.recvfrom(46080)
        temp+=data

        if len(temp) == (921600):
            frame = numpy.fromstring (temp,dtype=numpy.uint8)
            #import ipdb; ipdb.set_trace()
            frame = frame.reshape (480,640,3)
            nf = pygame.surfarray.make_surface(numpy.transpose(frame, (1,0,2)))
            #nf = pygame.surfarray.make_surface(frame)

            # Display the resulting frame
            screen.blit(nf, (CAMERA_RECT_X,CAMERA_RECT_Y))
            pygame.display.flip()
            # pygame.display.update()
            temp=""



