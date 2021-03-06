import pygame
from constants import *
from images import Images
from globalvars import *


class Canvas():
    def __init__(self):
        self.imgs, self.imgsdis = Images().get_images()
        self.cam_rect = pygame.Rect(CAMERA_POS, CAMERA_SIZE)

    def draw(self, screen):
        screen.fill(WHITE)
        for k, v in self.imgs.items():
            surface, rectangle = v
            screen.blit(surface, rectangle)
            pygame.draw.rect(screen, BLACK, self.cam_rect, 3)
        if get_possock() or get_camsock():
            for k, v in self.imgsdis.items():
                surface, rectangle = v
                screen.blit(surface, rectangle)
                get_clikd_btn() == "dc"

    def get_cam_rect(self):
        return self.cam_rect
