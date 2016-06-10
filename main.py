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
        import ipdb; ipdb.set_trace()
        pygame.init()

        self.imgs = Images()
        self.canv = Canvas()
        self.netw = Network()
        self.fonts = Fonts()
        self.mouse = MouseControls()

        self.clicked_button = None
        self.images = None
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def main(self):
        self.imagens = imgs.load_images()

        while True:
            # Handling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sock.close()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    clicked_button = int(button_clicked(event.pos))
                    if clicked_button in range(0, NUMBER_MOVEMENTS):
                        if sock:
                            sock.send(bytes(str(clicked_button), 'UTF-8'))
                    elif clicked_button == NUMBER_MOVEMENTS and not sock:
                        sock = netw.connect_to_server()
                if event.type == MOUSEBUTTONUP:
                    clicked_button = None

            # Drawing objects
            draw(sock)

if __name__ == '__main__':
    labarm = LabArm()
    labarm.main()
