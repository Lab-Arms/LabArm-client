import pygame

BUTTON_WIDTH = (110)
BUTTON_HEIGHT = (68)

ROBO_X = (200)
ROBO_Y = (30)

MOTOR1HORARIO_X = (203)
MOTOR1HORARIO_Y = (622)
MOTOR1ANTIHORARIO_X = (318)
MOTOR1ANTIHORARIO_Y = (622)

MOTOR2HORARIO_X = (20)
MOTOR2HORARIO_Y = (320)
MOTOR2ANTIHORARIO_X = (135)
MOTOR2ANTIHORARIO_Y = (320)

MOTOR3HORARIO_X = (185)
MOTOR3HORARIO_Y = (15)
MOTOR3ANTIHORARIO_X = (300)
MOTOR3ANTIHORARIO_Y = (15)

MOTOR4HORARIO_X = (595)
MOTOR4HORARIO_Y = (15)
MOTOR4ANTIHORARIO_X = (710)
MOTOR4ANTIHORARIO_Y = (15)

MOTOR5HORARIO_X = (850)
MOTOR5HORARIO_Y = (150)
MOTOR5ANTIHORARIO_X = (965)
MOTOR5ANTIHORARIO_Y = (150)


def load_images():
    imagens = {}

    robo_surface = pygame.image.load("img/pecas.bmp")
    horario_surface = pygame.image.load("img/horario.png")
    antihorario_surface = pygame.image.load("img/antihorario.png")

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
    motor5horario = horario_surface.get_rect()
    motor5horario.x = MOTOR5HORARIO_X
    motor5horario.y = MOTOR5HORARIO_Y
    imagens[9] = (horario_surface, motor5horario)
    motor5antihorario = antihorario_surface.get_rect()
    motor5antihorario.x = MOTOR5ANTIHORARIO_X
    motor5antihorario.y = MOTOR5ANTIHORARIO_Y
    imagens[10] = (antihorario_surface, motor5antihorario)

    return imagens
