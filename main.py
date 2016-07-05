#!/usr/bin/env python
import pygame
from pygame.locals import *

from constants import SCREEN_SIZE
from canvas import Canvas
from constants import *
from events import PCEvents
from fonts import Fonts
from images import Images
from network import Network
from buttons import Buttons


class LabArm():
    def __init__(self):
        pygame.init()

        self.imgs = Images()
        self.canvas = Canvas()
        self.netw = Network()
        self.fonts = Fonts()
        self.events = PCEvents()
        self.buttons = Buttons()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def run(self):
        while True:
            self.events.handle(self.screen, self.netw)
            self.canvas.draw(self.screen)
            self.buttons.draw(self.screen)
            self.fonts.draw(self.screen)
            self.netw.draw(self.screen)
            pygame.display.flip()

if __name__ == '__main__':
    labarm = LabArm()
    labarm.run()
