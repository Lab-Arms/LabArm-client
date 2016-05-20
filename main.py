import sys
import pygame
from pygame.locals import *
import res

pygame.init()

size = width, height = 1200, 700
white = 254, 254, 254

screen = pygame.display.set_mode(size)

clicked = False
imagens = {}


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
    imagens = res.load_images()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # event.pos retorna uma tupla
                import ipdb; ipdb.set_trace()
                clicked = True
            if event.type == MOUSEBUTTONUP:
                clicked = False

        draw()

if __name__ == '__main__':
    main()
