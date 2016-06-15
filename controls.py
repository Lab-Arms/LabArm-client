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
            x > MOTOR1_X and x < MOTOR1_X + BUTTON_WIDTH and
            y > MOTOR1_Y and y < MOTOR1_Y + BUTTON_HEIGHT
        ):
            return "a"
        elif (
            x > MOTOR2_X and x < MOTOR2_X + BUTTON_WIDTH and
            y > MOTOR2_Y and y < MOTOR2_Y + BUTTON_HEIGHT
        ):
            return "b"
        elif (
            x > MOTOR3_X and x < MOTOR3_X + BUTTON_WIDTH and
            y > MOTOR3_Y and y < MOTOR3_Y + BUTTON_HEIGHT
        ):
            return "c"
        elif (
            x > MOTOR4_X and x < MOTOR4_X + BUTTON_WIDTH and
            y > MOTOR4_Y and y < MOTOR4_Y + BUTTON_HEIGHT
        ):
            return "d"
        elif (
            x > MOTOR5ABRIR_X and x < MOTOR5ABRIR_X + BUTTON_WIDTH and
            y > MOTOR5ABRIR_Y and y < MOTOR5ABRIR_Y + BUTTON_HEIGHT
        ):
            return "ea"
        elif (
            x > MOTOR5FECHAR_X and x < MOTOR5FECHAR_X + BUTTON_WIDTH and
            y > MOTOR5FECHAR_Y and y < MOTOR5FECHAR_Y + BUTTON_HEIGHT
        ):
            return "ef"

        elif (
            x > CAMERA_RECT_X and x < CAMERA_RECT_X + CAMERA_RECT_WIDTH and
            y > CAMERA_RECT_Y and y < CAMERA_RECT_Y + CAMERA_RECT_HEIGHT
        ):
            return "cam"
        
        elif (
            x > DISCONNECT_RECT_X and x < DISCONNECT_RECT_X + DISCONNECT_RECT_WIDTH and
            y > DISCONNECT_RECT_Y and y < DISCONNECT_RECT_Y + DISCONNECT_RECT_HEIGHT
        ):
            return "disconnect"

        else:
            return None
