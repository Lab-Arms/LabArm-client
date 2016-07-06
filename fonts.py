import pygame
from constants import BLACK
from canvas import Canvas
from globalvars import *
from buttons import Buttons


class Fonts(Canvas):
    def __init__(self):
        canv = Canvas()
        btn = Buttons()
        self.cam = canv.get_cam_rect()
        self.btn0 = btn.get_button0()
        self.btn1 = btn.get_button1()
        self.btn2 = btn.get_button2()
        self.btn3 = btn.get_button3()
        self.abrir = btn.get_button4()
        self.fechar = btn.get_button5()
        self.disc = btn.get_disconect()
        self.font = pygame.font.SysFont("timesnewroman", 18)
        self.disc_text = self.font.render(
            "Desconectado do servidor.", True, BLACK)
        self.conn_text = self.font.render(
            "Deseja conectar?", True, BLACK)
        self.disconnect_text = self.font.render(
            "Desconectar", True, BLACK)
        self.button0 = self.font.render("Pos Inicial", True, BLACK)
        self.button1 = self.font.render("Tubo Ensaio", True, BLACK)
        self.button2 = self.font.render("Becker AO", True, BLACK)
        self.button3 = self.font.render("Becker AC", True, BLACK)
        self.button4 = self.font.render("Elem Gelo", True, BLACK)
        self.button5 = self.font.render("Filtro", True, BLACK)

    def draw(self, screen):
        if not get_possock() or get_possock() == -1:
            screen.blit(
                self.disc_text, (
                    self.cam.centerx - self.disc_text.get_width() / 2,
                    self.cam.centery - 25 - self.disc_text.get_height() / 2
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
                self.disconnect_text, (
                    self.disc.centerx - self.disconnect_text.get_width() / 2,
                    self.disc.centery - self.disconnect_text.get_height() / 2
                )
            )
            pygame.draw.rect(screen, BLACK, self.disc, 2)

        screen.blit(
            self.button0, (
                self.btn0.centerx - self.button0.get_width() / 2,
                self.btn0.centery - self.button0.get_height() / 2
                )
            )
        screen.blit(
            self.button1, (
                self.btn1.centerx - self.button1.get_width() / 2,
                self.btn1.centery - self.button1.get_height() / 2
                )
            )
        screen.blit(
            self.button2, (
                self.btn2.centerx - self.button2.get_width() / 2,
                self.btn2.centery - self.button2.get_height() / 2
                )
            )
        screen.blit(
            self.button3, (
                self.btn3.centerx - self.button3.get_width() / 2,
                self.btn3.centery - self.button3.get_height() / 2
                )
            )
        screen.blit(
            self.button4, (
                self.abrir.centerx - self.button4.get_width() / 2,
                self.abrir.centery - self.button4.get_height() / 2
                )
            )
        screen.blit(
            self.button5, (
                self.fechar.centerx - self.button5.get_width() / 2,
                self.fechar.centery - self.button5.get_height() / 2
                )
                self.abrir.centerx - self.button5.get_width() / 2,
                self.abrir.centery - self.button5.get_height() / 2
            )
        screen.blit(
            self.button6, (
                self.fechar.centerx - self.button6.get_width() / 2,
                self.fechar.centery - self.button6.get_height() / 2
            )
        )
