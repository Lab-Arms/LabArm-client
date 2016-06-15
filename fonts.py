import pygame
from constants import BLACK
from canvas import Canvas
from globalvars import *

from camera import VideoCamera


class Fonts(Canvas):
    def __init__(self):
        canv = Canvas()
        self.cam = canv.get_cam_rect()
        self.font = pygame.font.SysFont("timesnewroman", 54)
        self.disc_text = self.font.render(
            "Desconectado do servidor.", True, BLACK)
        self.conn_text = self.font.render(
            "Deseja conectar?", True, BLACK)
        self.succ_text = self.font.render("Conectado!", True, BLACK)

    def draw(self, screen):
        if not get_sock() or get_sock() == -1:
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
            pass
            #screen.blit(
            #    self.disc2_text, (
            #        self.disc.centerx - self.disc2_text.get_width() / 2,
            #        self.disc.centery - self.disc2_text.get_height() / 2
            #    )
            #)
            #pygame.draw.rect(screen, BLACK, self.disc, 2)
            

    # def gen(camera):
    #    while True:
    #        frame = camera.get_frame()
    #        yield (b'--frame\r\n'
    #               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    # def video_feed():
    #    return Response(gen(VideoCamera()),
    #                    mimetype='multipart/x-mixed-replace; boundary=frame')