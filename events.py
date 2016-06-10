import sys
import pygame
from pygame.locals import *
from controls import PCControls
from constants import ESTADO_MOTORES
from globalvars import *


class PCEvents(PCControls):
    def __init__(self):
        self.ctrls = PCControls()

    def handle(self, netw):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if get_sock():
                    get_sock().close()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                set_clikd_btn(self.ctrls.button_clicked(event.pos))
                if get_clikd_btn() in ESTADO_MOTORES:
                    if get_sock():
                        get_sock().send(bytes(get_clikd_btn(), 'UTF-8'))
                elif (get_clikd_btn() == 'cam' and not get_sock()):
                    set_sock(netw.connect_to_server())
            if event.type == MOUSEBUTTONUP:
                set_clikd_btn(None)
