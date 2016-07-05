import pygame
from constants import *
from globalvars import *


class Buttons():
    def __init__(self):
        self.btn_dict = {}
        self.motor1 = pygame.Rect(BUTTON0_POS, BUTTON_SIZE)
        self.btn_dict['a'] = self.motor1
        self.motor2 = pygame.Rect(BUTTON1_POS, BUTTON_SIZE)
        self.btn_dict['b'] = self.motor2
        self.motor3 = pygame.Rect(BUTTON2_POS, BUTTON_SIZE)
        self.btn_dict['c'] = self.motor3
        self.motor4 = pygame.Rect(BUTTON3_POS, BUTTON_SIZE)
        self.btn_dict['d'] = self.motor4
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

    def get_button1(self):
        return self.motor1

    def get_button2(self):
        return self.motor2

    def get_button3(self):
        return self.motor3

    def get_button4(self):
        return self.motor4

    def get_button5(self):
        return self.abrir

    def get_button6(self):
        return self.fechar
    
    def get_disconect(self):
        return self.disconect
