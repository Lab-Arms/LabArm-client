import pygame
from constants import *


class Images():
    def __init__(self):
        self.imagens = {}
        self.imagens_conn = {}

        self.robo_surface = pygame.image.load("img/arm.png")

        self.robo = self.robo_surface.get_rect()
        self.robo.x = ROBO_X
        self.robo.y = ROBO_Y
        self.imagens['bg'] = (self.robo_surface, self.robo)

    def get_images(self):
        return self.imagens, self.imagens_conn
