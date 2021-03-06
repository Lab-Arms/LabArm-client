from constants import *


class Controls():
    def __init__(self):
        pass


class PCControls(Controls):
    def __init__(self):
        pass

    def button_clicked(self, pos):
        x, y = pos

        if (
            x > BUTTON0_X and x < BUTTON0_X + BUTTON_WIDTH and
            y > BUTTON0_Y and y < BUTTON0_Y + BUTTON_HEIGHT
        ):
            return "a"
        elif (
            x > BUTTON1_X and x < BUTTON1_X + BUTTON_WIDTH and
            y > BUTTON1_Y and y < BUTTON1_Y + BUTTON_HEIGHT
        ):
            return "b"
        elif (
            x > BUTTON2_X and x < BUTTON2_X + BUTTON_WIDTH and
            y > BUTTON2_Y and y < BUTTON2_Y + BUTTON_HEIGHT
        ):
            return "c"
        elif (
            x > BUTTON3_X and x < BUTTON3_X + BUTTON_WIDTH and
            y > BUTTON3_Y and y < BUTTON3_Y + BUTTON_HEIGHT
        ):
            return "d"
        elif (
            x > ABRIR_X and x < ABRIR_X + BUTTON_WIDTH and
            y > ABRIR_Y and y < ABRIR_Y + BUTTON_HEIGHT
        ):
            return "e"
        elif (
            x > FECHAR_X and x < FECHAR_X + BUTTON_WIDTH and
            y > FECHAR_Y and y < FECHAR_Y + BUTTON_HEIGHT
        ):
            return "f"

        elif (
            x > CAMERA_X and x < CAMERA_X + CAMERA_WIDTH and
            y > CAMERA_Y and y < CAMERA_Y + CAMERA_HEIGHT
        ):
            return "cam"

        elif (
            x > DISC_CONN_X and x < DISC_CONN_X + DISC_CONN_WIDTH and
            y > DISC_CONN_Y and y < DISC_CONN_Y + DISC_CONN_HEIGHT
        ):
            return "dc"

        else:
            return None
