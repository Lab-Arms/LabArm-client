import pygame
from constants import *


class Images():
    def __init__(self):
        self.imagens = {}

        self.robo_surface = pygame.image.load("img/arm.png")
        self.horario_surface = pygame.image.load("img/horario.png")
        self.antihorario_surface = pygame.image.load("img/antihorario.png")
        self.abrir_surface = pygame.image.load("img/abrir.png")
        self.fechar_surface = pygame.image.load("img/fechar.png")

        self.robo = self.robo_surface.get_rect()
        self.robo.x = ROBO_X
        self.robo.y = ROBO_Y
        self.imagens[0] = (self.robo_surface, self.robo)

        # setas motor 1
        self.motor1horario = self.horario_surface.get_rect()
        self.motor1horario.x = MOTOR1HORARIO_X
        self.motor1horario.y = MOTOR1HORARIO_Y
        self.imagens[1] = (self.horario_surface, self.motor1horario)

        # setas motor 2
        self.motor2horario = self.horario_surface.get_rect()
        self.motor2horario.x = MOTOR2HORARIO_X
        self.motor2horario.y = MOTOR2HORARIO_Y
        self.imagens[2] = (self.horario_surface, self.motor2horario)

        # setas motor 3
        self.motor3horario = self.horario_surface.get_rect()
        self.motor3horario.x = MOTOR3HORARIO_X
        self.motor3horario.y = MOTOR3HORARIO_Y
        self.imagens[3] = (self.horario_surface, self.motor3horario)

        # setas motor 4
        self.motor4horario = self.horario_surface.get_rect()
        self.motor4horario.x = MOTOR4HORARIO_X
        self.motor4horario.y = MOTOR4HORARIO_Y
        self.imagens[4] = (self.horario_surface, self.motor4horario)
        self.motor4antihorario = self.antihorario_surface.get_rect()
        self.motor4antihorario.x = MOTOR4ANTIHORARIO_X
        self.motor4antihorario.y = MOTOR4ANTIHORARIO_Y
        self.imagens[5] = (self.antihorario_surface, self.motor4antihorario)

        # setas motor 5
        self.motor5abrir = self.abrir_surface.get_rect()
        self.motor5abrir.x = MOTOR5ABRIR_X
        self.motor5abrir.y = MOTOR5ABRIR_Y
        self.imagens[6] = (self.abrir_surface, self.motor5abrir)
        self.motor5fechar = self.fechar_surface.get_rect()
        self.motor5fechar.x = MOTOR5FECHAR_X
        self.motor5fechar.y = MOTOR5FECHAR_Y
        self.imagens[7] = (self.fechar_surface, self.motor5fechar)

    def get_images(self):
        return self.imagens
