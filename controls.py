from constants import *


class Controls():
    def __init__(self):
        pass


class PCControls(Controls):
    def __init__(self):
        pass

    def button_clicked(self, pos):
        x, y = pos
        # Identifying button clicked
        # Motor 1 buttons
        if (
            x > MOTOR1_X and x < MOTOR1_X + BUTTON_WIDTH and
            y > MOTOR1_Y and y < MOTOR1_Y + BUTTON_HEIGHT
        ):
            return "a"

        # Motor 2 buttons
        elif (
            x > MOTOR2_X and x < MOTOR2_X + BUTTON_WIDTH and
            y > MOTOR2_Y and y < MOTOR2_Y + BUTTON_HEIGHT
        ):
            return "b"

        # Motor 3 buttons
        elif (
            x > MOTOR3_X and x < MOTOR3_X + BUTTON_WIDTH and
            y > MOTOR3_Y and y < MOTOR3_Y + BUTTON_HEIGHT
        ):
            return "c"

        # Motor 4 buttons
        elif (
            x > MOTOR4_X and x < MOTOR4_X + BUTTON_WIDTH and
            y > MOTOR4_Y and y < MOTOR4_Y + BUTTON_HEIGHT
        ):
            return "d"

        # Motor 5 buttons
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

        else:
            return None
