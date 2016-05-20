import sys
import pygame
from pygame.locals import *

pygame.init()

size = width, height = 1200, 700
white = 254, 254, 254

screen = pygame.display.set_mode(size)

clicked = False
imagens = {}


def load_images():
    robo = pygame.image.load("img/pecas.bmp")
    roborect = robo.get_rect()
    roborect.x = 200
    roborect.y = 30
    imagens[0] = (robo, roborect)

    horario = pygame.image.load("img/horario.png")
    horariorect = horario.get_rect()
    horariorect.x = 20
    horariorect.y = 320
    imagens[1] = (horario, horariorect)

    antihorario = pygame.image.load("img/antihorario.png")
    antihorariorect = antihorario.get_rect()
    antihorariorect.x = 25 + antihorariorect.width
    antihorariorect.y = 320
    imagens[2] = (antihorario, antihorariorect)


def draw():
    screen.fill(white)
    if not clicked:
        for k, v in imagens.items():
            #import ipdb; ipdb.set_trace()
            i, r = v
            screen.blit(i, r)
    pygame.display.flip()


def main():
    global clicked
    load_images()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                clicked = True
            if event.type == MOUSEBUTTONUP:
                clicked = False

        draw()

if __name__ == '__main__':
    main()
