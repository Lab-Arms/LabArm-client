import pygame
from constants import CAMERA_SIZE

global g_clikd_btn
global g_sock
global g_camsurface

g_clikd_btn = None
g_camsock = None
g_possock = None
g_con = True
g_camsurface = pygame.Surface(CAMERA_SIZE)


def get_clikd_btn():
    global g_clikd_btn
    return g_clikd_btn


def get_camsock():
    global g_possock
    return g_possock


def get_possock():
    global g_possock
    return g_possock


def get_con():
    global g_con
    return g_con


def get_camera_surface():
    global g_camsurface
    return g_camsurface


def set_clikd_btn(btn):
    global g_clikd_btn
    g_clikd_btn = btn


def set_possock(sock):
    global g_possock
    g_possock = sock


def set_camsock(sock):
    global g_camsock
    g_camsock = sock


def set_con(con):
    global g_con
    g_con = con


def set_camera_surface(surface):
    global g_camsurface
    g_camsurface = surface


def empty_camera_surface():
    s = pygame.Surface(CAMERA_SIZE)
    set_camera_surface(s)
