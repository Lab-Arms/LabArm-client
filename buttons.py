import pygame
from constants import *
from globalvars import *


class Buttons():
    def __init__(self):
        self.btn_dict = {}
        self.btn0 = pygame.Rect(BUTTON0_POS, BUTTON_SIZE)
        self.btn_dict['a'] = self.btn0
        self.btn1 = pygame.Rect(BUTTON1_POS, BUTTON_SIZE)
        self.btn_dict['b'] = self.btn1
        self.btn2 = pygame.Rect(BUTTON2_POS, BUTTON_SIZE)
        self.btn_dict['c'] = self.btn2
        self.btn3 = pygame.Rect(BUTTON3_POS, BUTTON_SIZE)
        self.btn_dict['d'] = self.btn3
        self.abrir = pygame.Rect(ABRIR_POS, BUTTON_SIZE)
        self.btn_dict['ea'] = self.abrir
        self.fechar = pygame.Rect(FECHAR_POS, BUTTON_SIZE)
        self.btn_dict['ef'] = self.fechar
        self.disconect = pygame.Rect(DISC_CONN_POS, DISC_CONN_SIZE)
        self.btn_dict['dc'] = self.disconect

    def draw(self, screen):
        for k, v in self.btn_dict.items():
            screen.fill(WHITE, v)
            pygame.draw.rect(screen, BLACK, v, 3)
        if (
            get_clikd_btn() and
            get_clikd_btn() in ESTADO_MOTORES
        ):
            rectangle = self.btn_dict[get_clikd_btn()]
            screen.fill(GRAY, rectangle)
            pygame.draw.rect(screen, BLACK, rectangle, 3)

    def get_button0(self):
        return self.btn0

    def get_button1(self):
        return self.btn1

    def get_button2(self):
        return self.btn2

    def get_button3(self):
        return self.btn3

    def get_button4(self):
        return self.abrir

    def get_button5(self):
        return self.fechar
    
    def get_disconect(self):
        return self.disconect
