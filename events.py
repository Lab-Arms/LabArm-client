import sys
import pygame
from pygame.locals import *
from controls import PCControls
from constants import ESTADO_MOTORES
from globalvars import *


class PCEvents(PCControls):
    def __init__(self):
        self.ctrls = PCControls()
        self.angle_value = ''
        self.angle_dict = {}

    def handle(self, netw):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if get_sock():
                    get_sock().close()
                sys.exit()

            if not get_clikd_btn() and event.type == MOUSEBUTTONDOWN:
                set_clikd_btn(self.ctrls.button_clicked(event.pos))

            if event.type == KEYDOWN:
                if event.key in range(K_0, K_9 + 1):
                    self.angle_value += str(event.key - K_0)
                if get_clikd_btn() and event.key == K_RETURN:
                    self.angle_dict[get_clikd_btn()] = self.angle_value
                    self.angle_value = ''
                    set_clikd_btn(None)
                if event.key == K_ESCAPE:
                    # TODO: Mudar evento para mouse click
                    pass

            if (get_clikd_btn() == 'cam' and not get_sock()):
                 set_sock(netw.connect_to_server())
