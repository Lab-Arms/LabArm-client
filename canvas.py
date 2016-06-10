import pygame
from constants import *
from images import Images
from globalvars import *


class Canvas():
    def __init__(self):
        self.imgs = Images().get_images()
        self.cam_rect = pygame.Rect(450, 250, 732, 450)
        self.disc_rect = pygame.Rect(1000, 20, 170, 35)

    def draw(self, screen):
        screen.fill(WHITE)
        if (
            get_clikd_btn() is not None and
            get_clikd_btn() in ESTADO_MOTORES
        ):
            _, rectangle = self.imgs[get_clikd_btn()]
            screen.fill(GRAY, rectangle)
        for k, v in self.imgs.items():
            surface, rectangle = v
            screen.blit(surface, rectangle)
            pygame.draw.rect(screen, BLACK, self.cam_rect, 3)

    def get_cam_rect(self):
        return self.cam_rect

    def get_disc_rect(self):
        return self.disc_rect
