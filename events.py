import sys
import collections
import pygame
from pygame.locals import *
from controls import PCControls
from globalvars import *
from network import Network


class PCEvents(PCControls):
    def __init__(self):
        self.ctrls = PCControls()
        self.angle_value = ''
        self.angle_dict = {
            'a': '090', 'b': '170', 'c': '090', 'd': '090', 'e': '090'
        }
        self.final_string = ''
        self.changed_value = False

    def handle(self, screen, netw):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if get_sock():
                    get_sock().close()
                sys.exit()

            if not get_clikd_btn() and event.type == MOUSEBUTTONDOWN:
                set_clikd_btn(self.ctrls.button_clicked(event.pos))

            if event.type == KEYDOWN:
                if event.key in range(K_0, K_9 + 1):
                    if len(self.angle_value) < 3:
                        self.changed_value = True
                        self.angle_value += str(event.key - K_0)
                    else:
                        print("valor para ângulo maior que 3, informe valor menor que 3")
                if get_clikd_btn() and event.key == K_RETURN:
                    self.angle_dict[get_clikd_btn()] = self.angle_value
                    self.angle_value = ''
                    set_clikd_btn(None)
                if event.key == K_ESCAPE:
                    if self.changed_value and get_sock():
                        self.final_string = ''
                        # TODO: Mudar evento para mouse click
                        ordered = collections.OrderedDict(
                            sorted(self.angle_dict.items())
                        )
                        self.final_string = " ".join(
                            str(v) for _, v in ordered.items()
                        )
                        self.changed_value = False
                        get_sock().send(bytes(self.final_string, 'UTF-8'))

            if (get_clikd_btn() == 'cam' and not get_sock()):
                set_sock(netw.connect_to_server(screen))
                set_clikd_btn(None)


            if (get_clikd_btn() == 'disconnect' and get_sock()):
                set_sock(netw.disconnect_from_server())
                set_clikd_btn(None)
                 
#    if value in range(0, 180):
