#!/usr/bin/env python
import sys
import pygame
from pygame.locals import *
from controls import *

from network import Network
from images import Images
from canvas import Canvas
from fonts import Fonts
from controls import MouseControls


class LabArm():
    def __init__(self):
        pygame.init()

        self.imgs = Images()
        self.canv = Canvas()
        self.netw = Network()
        self.fonts = Fonts()
        self.mouse = MouseControls()

        self.clicked_button = None
        self.images = None
        self.sock = None
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def main(self):
        self.images = self.imgs.get_images()
        while True:
            # Handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.sock.close()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    self.clicked_button = int(self.button_clicked(event.pos))
                    if self.clicked_button in range(0, NUMBER_MOVEMENTS):
                        if self.sock:
                            self.sock.send(
                                bytes(str(self.clicked_button), 'UTF-8'))
                    elif (
                        self.clicked_button == NUMBER_MOVEMENTS and
                        not self.sock
                    ):
                        self.sock = self.netw.connect_to_server()
                if event.type == MOUSEBUTTONUP:
                    self.clicked_button = None

            # Drawing objects
            self.canv.draw(self.screen, self.images, self.clicked_button)
            self.fonts.draw(self.screen, self.sock)
            pygame.display.flip()

if __name__ == '__main__':
    labarm = LabArm()
    labarm.main()
