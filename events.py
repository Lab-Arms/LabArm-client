import sys
import pygame
from pygame.locals import *
from controls import PCControls
from constants import ESTADO_MOTORES


class PCEvents(PCControls):
    def __init__(self):
        self.ctrls = PCControls()
        self.sock = None

    def handle(self, netw, clikd_btn):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.sock:
                        self.sock.close()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    self.clikd_btn = self.ctrls.button_clicked(event.pos)
                    if self.clikd_btn in ESTADO_MOTORES:
                        if self.sock:
                            self.sock.send(bytes(self.clikd_btn, 'UTF-8'))
                    elif (self.clikd_btn == 'cam' and not self.sock):
                        self.sock = netw.connect_to_server()
                if event.type == MOUSEBUTTONUP:
                    self.clikd_btn = None
