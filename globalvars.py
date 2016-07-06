import pygame
from constants import CAMERA_SIZE

global g_clikd_btn
global g_sock
global g_camsurface

g_clikd_btn = None
g_sock = None
g_con = True
g_camsurface = pygame.Surface(CAMERA_SIZE)


def get_clikd_btn():
    global g_clikd_btn
    return g_clikd_btn


def get_sock():
    global g_sock
    return g_sock


def get_con():
    global g_con
    return g_con


def get_camera_surface():
    global g_camsurface
    return g_camsurface


def set_clikd_btn(btn):
    global g_clikd_btn
    g_clikd_btn = btn


def set_sock(sock):
    global g_sock
    g_sock = sock


def set_con(con):
    global g_con
    g_con = con


def set_camera_surface(surface):
    global g_camsurface
    g_camsurface = surface


def empty_camera_surface():
    s = pygame.Surface(CAMERA_SIZE)
    set_camera_surface(s)
