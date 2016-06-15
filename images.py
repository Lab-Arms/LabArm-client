import pygame
from constants import *


class Images():
    def __init__(self):
        self.imagens = {}
        self.imagens_conn = {}

        self.robo_surface = pygame.image.load("img/arm.png")
        self.horario_surface = pygame.image.load("img/horario.png")
        self.antihorario_surface = pygame.image.load("img/antihorario.png")
        self.abrir_surface = pygame.image.load("img/abrir.png")
        self.fechar_surface = pygame.image.load("img/fechar.png")
        self.desconectar_surface = pygame.image.load("img/desconectar.png")

        self.robo = self.robo_surface.get_rect()
        self.robo.x = ROBO_X
        self.robo.y = ROBO_Y
        self.imagens['bg'] = (self.robo_surface, self.robo)

        self.motor1horario = self.horario_surface.get_rect()
        self.motor1horario.x = MOTOR1_X
        self.motor1horario.y = MOTOR1_Y
        self.imagens['a'] = (self.horario_surface, self.motor1horario)

        self.motor2horario = self.horario_surface.get_rect()
        self.motor2horario.x = MOTOR2_X
        self.motor2horario.y = MOTOR2_Y
        self.imagens['b'] = (self.horario_surface, self.motor2horario)

        self.motor3horario = self.horario_surface.get_rect()
        self.motor3horario.x = MOTOR3_X
        self.motor3horario.y = MOTOR3_Y
        self.imagens['c'] = (self.horario_surface, self.motor3horario)

        self.motor4horario = self.horario_surface.get_rect()
        self.motor4horario.x = MOTOR4_X
        self.motor4horario.y = MOTOR4_Y
        self.imagens['d'] = (self.horario_surface, self.motor4horario)

        self.motor5abrir = self.abrir_surface.get_rect()
        self.motor5abrir.x = MOTOR5ABRIR_X
        self.motor5abrir.y = MOTOR5ABRIR_Y
        self.imagens['ea'] = (self.abrir_surface, self.motor5abrir)
        self.motor5fechar = self.fechar_surface.get_rect()
        self.motor5fechar.x = MOTOR5FECHAR_X
        self.motor5fechar.y = MOTOR5FECHAR_Y
        self.imagens['ef'] = (self.fechar_surface, self.motor5fechar)

        self.desconectar = self.desconectar_surface.get_rect()
        self.desconectar.x = DISCONNECT_RECT_X
        self.desconectar.y = DISCONNECT_RECT_Y
        self.imagens_conn['dc'] = (self.desconectar_surface, self.desconectar)

    def get_images(self):
        return self.imagens, self.imagens_conn
