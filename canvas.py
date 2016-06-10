import pygame
from constants import *


class Canvas():
    def __init__(self):
        self.cam_rect = pygame.Rect(450, 250, 732, 450)
        self.disc_rect = pygame.Rect(1000, 20, 170, 35)

    def draw(self, screen, imgs, clikd_btn):
        screen.fill(WHITE)
        if (
            clikd_btn is not None and
            clikd_btn in range(0, NUMBER_MOVEMENTS)
        ):
            # XXX: O Índice está errado
            _, rectangle = imgs[clikd_btn + 1]
            screen.fill(gray, rectangle)
        for k, v in imgs.items():
            surface, rectangle = v
            screen.blit(surface, rectangle)
            pygame.draw.rect(screen, BLACK, self.cam_rect, 3)

    def get_cam_rect(self):
        return self.cam_rect

    def get_disc_rect(self):
        return self.disc_rect
