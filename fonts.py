import pygame
from constants import BLACK
from canvas import Canvas
from globalvars import *


class Fonts(Canvas):
    def __init__(self):
        canv = Canvas()
        self.cam = canv.get_cam_rect()
        self.disc = canv.get_disc_rect()
        self.font1 = pygame.font.SysFont("timesnewroman", 54)
        self.font2 = pygame.font.SysFont("timesnewroman", 30)
        self.disc1_text = self.font1.render(
            "Desconectado do servidor.", True, BLACK)
        self.conn_text = self.font1.render(
            "Deseja conectar?", True, BLACK)
        self.succ_text = self.font1.render("Conectado!", True, BLACK)
        self.disc2_text = self.font2.render("Desconectar", True, BLACK)

    def draw(self, screen):
        if not get_sock() or get_sock() == -1 or get_sock()._closed:
            screen.blit(
                self.disc1_text, (
                    self.cam.centerx - self.disc1_text.get_width() / 2,
                    self.cam.centery - 25 - self.disc1_text.get_height() / 2
                )
            )
            screen.blit(
                self.conn_text, (
                    self.cam.centerx - self.conn_text.get_width() / 2,
                    self.cam.centery + 25 - self.conn_text.get_height() / 2
                )
            )
        else:
            screen.blit(
                self.succ_text, (
                    self.cam.centerx - self.succ_text.get_width() / 2,
                    self.cam.centery - self.succ_text.get_height() / 2
                )
            )
            screen.blit(
                self.disc2_text, (
                    self.disc.centerx - self.disc2_text.get_width() / 2,
                    self.disc.centery - self.disc2_text.get_height() / 2
                )
            )
            pygame.draw.rect(screen, BLACK, self.disc, 2)
