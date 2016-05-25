#!/usr/bin/env python

import sys
import pygame
from pygame.locals import *
from images import *
from constants import *
from controls import *

pygame.init()

size = width, height = 1200, 700
white = 254, 254, 254
clicked = None

screen = pygame.display.set_mode(size)


def draw():
    screen.fill(white)
    if not clicked:
        for k, v in imagens.items():
            i, r = v
            screen.blit(i, r)
    pygame.display.flip()


def main():
    global clicked
    global imagens

    imagens = load_images()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                clicked = button_clicked(event.pos)
                if clicked:
                    print(clicked)
            if event.type == MOUSEBUTTONUP:
                clicked = None

        draw()

if __name__ == '__main__':
    main()
