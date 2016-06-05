import pygame
from constants import *


def load_images():
    imagens = {}

    robo_surface = pygame.image.load("img/arm.png")
    horario_surface = pygame.image.load("img/horario.png")
    antihorario_surface = pygame.image.load("img/antihorario.png")
    abrir_surface = pygame.image.load("img/abrir.png")
    fechar_surface = pygame.image.load("img/fechar.png")

    robo = robo_surface.get_rect()
    robo.x = ROBO_X
    robo.y = ROBO_Y
    imagens[0] = (robo_surface, robo)

    # setas motor 1
    motor1horario = horario_surface.get_rect()
    motor1horario.x = MOTOR1HORARIO_X
    motor1horario.y = MOTOR1HORARIO_Y
    imagens[1] = (horario_surface, motor1horario)
    motor1antihorario = antihorario_surface.get_rect()
    motor1antihorario.x = MOTOR1ANTIHORARIO_X
    motor1antihorario.y = MOTOR1ANTIHORARIO_Y
    imagens[2] = (antihorario_surface, motor1antihorario)

    # setas motor 2
    motor2horario = horario_surface.get_rect()
    motor2horario.x = MOTOR2HORARIO_X
    motor2horario.y = MOTOR2HORARIO_Y
    imagens[3] = (horario_surface, motor2horario)
    motor2antihorario = antihorario_surface.get_rect()
    motor2antihorario.x = MOTOR2ANTIHORARIO_X
    motor2antihorario.y = MOTOR2ANTIHORARIO_Y
    imagens[4] = (antihorario_surface, motor2antihorario)

    # setas motor 3
    motor3horario = horario_surface.get_rect()
    motor3horario.x = MOTOR3HORARIO_X
    motor3horario.y = MOTOR3HORARIO_Y
    imagens[5] = (horario_surface, motor3horario)
    motor3antihorario = antihorario_surface.get_rect()
    motor3antihorario.x = MOTOR3ANTIHORARIO_X
    motor3antihorario.y = MOTOR3ANTIHORARIO_Y
    imagens[6] = (antihorario_surface, motor3antihorario)

    # setas motor 4
    motor4horario = horario_surface.get_rect()
    motor4horario.x = MOTOR4HORARIO_X
    motor4horario.y = MOTOR4HORARIO_Y
    imagens[7] = (horario_surface, motor4horario)
    motor4antihorario = antihorario_surface.get_rect()
    motor4antihorario.x = MOTOR4ANTIHORARIO_X
    motor4antihorario.y = MOTOR4ANTIHORARIO_Y
    imagens[8] = (antihorario_surface, motor4antihorario)

    # setas motor 5
    motor5abrir = abrir_surface.get_rect()
    motor5abrir.x = MOTOR5ABRIR_X
    motor5abrir.y = MOTOR5ABRIR_Y
    imagens[9] = (abrir_surface, motor5abrir)
    motor5fechar = fechar_surface.get_rect()
    motor5fechar.x = MOTOR5FECHAR_X
    motor5fechar.y = MOTOR5FECHAR_Y
    imagens[10] = (fechar_surface, motor5fechar)

    return imagens
