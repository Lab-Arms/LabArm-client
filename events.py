import sys
import collections
import pygame
from pygame.locals import *
from controls import PCControls
from globalvars import *


class PCEvents(PCControls):
    def __init__(self):
        self.ctrls = PCControls()

    def handle(self, screen, netw):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit(netw)

            if not get_clikd_btn() and event.type == MOUSEBUTTONDOWN:
                set_clikd_btn(self.ctrls.button_clicked(event.pos))
                get_sock().send(bytes(get_clikd_btn(), 'UTF-8'))

            if event.type == KEYDOWN:
                if event.key == pygame.K_c and \
                        pygame.key.get_mods() & pygame.KMOD_CTRL:
                    self.exit(netw)

            if (get_clikd_btn() == 'cam' and not get_sock()):
                set_sock(netw.connect_to_server())
                set_clikd_btn(None)
            if (get_clikd_btn() == 'dc' and get_sock()):
                set_sock(netw.disconnect_from_server())
                set_clikd_btn(None)

    def exit(self, netw):
        if get_sock():
            get_sock().close()
        sys.exit()
