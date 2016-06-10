import pygame
from constants import *


class Canvas():
    def __init__(self):
        import ipdb; ipdb.set_trace()
        self.cam_rect = pygame.Rect(450, 250, 732, 450)
        self.disc_rect = pygame.Rect(1000, 20, 170, 35)

    def draw(self, screen, sock, clicked_button):
        screen.fill(WHITE)
        if (
            clicked_button is not None and
            clicked_button in range(0, NUMBER_MOVEMENTS)
        ):
            _, rectangle = imagens[clicked_button + 1]
            screen.fill(gray, rectangle)
        for k, v in imagens.items():
            surface, rectangle = v
            screen.blit(surface, rectangle)
            pygame.draw.rect(screen, BLACK, cam_rect, 3)
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
            pygame.draw.rect(screen, BLACK, disc_rect, 2)
        pygame.display.flip()
