#!/usr/bin/env python
import pygame
from pygame.locals import *
from controls import *

from network import Network
from images import Images
from canvas import Canvas
from fonts import Fonts
from events import PCEvents


class LabArm():
    def __init__(self):
        pygame.init()

        self.imgs = Images()
        self.canv = Canvas()
        self.netw = Network()
        self.fonts = Fonts()
        self.events = PCEvents()

        self.clikd_btn = None
        self.images = None
        self.sock = None
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def run(self):
        self.images = self.imgs.get_images()
        while True:
            # XXX: clikd_btn não está sendo atualizado
            # XXX: sock também não está sendo atualizado
            # TODO: Transformar elas em lista e colocar em escopo global??
            self.events.handle(self.netw, self.clikd_btn)
            self.canv.draw(self.screen, self.images, self.clikd_btn)
            self.fonts.draw(self.screen, self.sock)
            pygame.display.flip()

if __name__ == '__main__':
    labarm = LabArm()
    labarm.run()
