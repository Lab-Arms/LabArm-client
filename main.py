#!/usr/bin/env python
import sys
import os
import pygame
import pygame.camera
import socket
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

clicked_button = None

screen = pygame.display.set_mode(size)
cam_rect = pygame.Rect(450, 250, 732, 450)
disc_rect = pygame.Rect(1000, 20, 170, 35)
font1 = pygame.font.SysFont("timesnewroman", 54)
font2 = pygame.font.SysFont("timesnewroman", 30)
disc1_text = font1.render("Desconectado do servidor.", True, black)
conn_text = font1.render("Deseja conectar?", True, black)
succ_text = font1.render("Conectado!", True, black)
disc2_text = font2.render("Desconectar", True, black)
connected = None


def draw(sock):
    screen.fill(white)
    if (
        clicked_button is not None and
        clicked_button in range(0, NUMBER_MOVEMENTS)
    ):
        _, rectangle = imagens[clicked_button + 1]
        screen.fill(gray, rectangle)
    for k, v in imagens.items():
        surface, rectangle = v
        screen.blit(surface, rectangle)
        pygame.draw.rect(screen, black, cam_rect, 3)
    if not sock or sock == -1 or sock._closed:
        screen.blit(
            disc1_text, (
                cam_rect.centerx - disc1_text.get_width() / 2,
                cam_rect.centery - 25 - disc1_text.get_height() / 2
            )
        )
        screen.blit(
            conn_text, (
                cam_rect.centerx - conn_text.get_width() / 2,
                cam_rect.centery + 25 - conn_text.get_height() / 2
            )
        )
    else:
        screen.blit(
            succ_text, (
                cam_rect.centerx - succ_text.get_width() / 2,
                cam_rect.centery - succ_text.get_height() / 2
            )
        )
        screen.blit(
            disc2_text, (
                disc_rect.centerx - disc2_text.get_width() / 2,
                disc_rect.centery - disc2_text.get_height() / 2
            )
        )
        pygame.draw.rect(screen, black, disc_rect, 2)
    pygame.display.flip()


def disconnect_from_server():
    pass


def connect_to_server():
    try:
        address = host, port = '127.0.0.1', 4004
        sock = socket.create_connection(address, timeout=10)
        sock.settimeout(None)
    except ConnectionRefusedError:
        sock = -1
    return sock


def main():
    global clicked_button
    global imagens
    sock = None

    imagens = load_images()

    while True:
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sock.close()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                clicked_button = int(button_clicked(event.pos))
                if clicked_button in range(0, NUMBER_MOVEMENTS):
                    sock.send(bytes(str(clicked_button), 'UTF-8'))
                elif clicked_button == NUMBER_MOVEMENTS and not sock:
                    sock = connect_to_server()
            if event.type == MOUSEBUTTONUP:
                clicked_button = None

        # Drawing objects
        draw(sock)

if __name__ == '__main__':
    main()
