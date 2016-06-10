import pygame
from constants import BLACK


class Fonts():
    def __init__(self):
        self.font1 = pygame.font.SysFont("timesnewroman", 54)
        self.font2 = pygame.font.SysFont("timesnewroman", 30)
        self.disc1_text = self.font1.render(
            "Desconectado do servidor.", True, BLACK)
        self.conn_text = self.font1.render(
            "Deseja conectar?", True, BLACK)
        self.succ_text = self.font1.render("Conectado!", True, BLACK)
        self.disc2_text = self.font2.render("Desconectar", True, BLACK)

    def draw_fonts():
        pass
