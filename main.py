#!/usr/bin/env python

import sys
import pygame
import pygame.camera
from pygame.locals import *
from images import *
from controls import *

pygame.init()
clock = pygame.time.Clock()
# pygame.camera.init()
# camm = pygame.camera.Camera("/dev/video0", (640, 480))
# camm.start()
# img = camm.get_image()
# screen.blit(img, cam)
# camm.stop()

size = width, height = 1200, 715
white = 254, 254, 254
gray = 200, 200, 200
black = 0, 0, 0

clicked = None

screen = pygame.display.set_mode(size)
cam_rect = pygame.Rect(450, 250, 732, 450)
font = pygame.font.SysFont("timesnewroman", 54)
text1 = font.render("Desconectado do servidor.", True, black)
text2 = font.render("Deseja conectar?", True, black)


def draw():
    screen.fill(white)
    if clicked:
        _, rectangle = imagens[int(clicked) + 1]
        screen.fill(gray, rectangle)
    for k, v in imagens.items():
        surface, rectangle = v
        screen.blit(surface, rectangle)

    pygame.draw.rect(screen, black, cam_rect, 3)
    screen.blit(text1, (cam_rect.centerx - text1.get_width() / 2, cam_rect.centery-25 - text1.get_height() / 2, ))
    screen.blit(text2, (cam_rect.centerx - text2.get_width() / 2, cam_rect.centery+25 - text2.get_height() / 2, ))
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
