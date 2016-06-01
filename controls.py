from constants import *


def button_clicked(pos):
    x, y = pos
    # Identifying button clicked
    # Motor 1 buttons
    if (
        x > MOTOR1HORARIO_X and x < MOTOR1HORARIO_X + BUTTON_WIDTH and
        y > MOTOR1HORARIO_Y and y < MOTOR1HORARIO_Y + BUTTON_HEIGHT
    ):
        return "0"
    elif (
        x > MOTOR1ANTIHORARIO_X and x < MOTOR1ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR1ANTIHORARIO_Y and y < MOTOR1ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "1"

    # Motor 2 buttons
    elif (
        x > MOTOR2HORARIO_X and x < MOTOR2HORARIO_X + BUTTON_WIDTH and
        y > MOTOR2HORARIO_Y and y < MOTOR2HORARIO_Y + BUTTON_HEIGHT
    ):
        return "2"
    elif (
        x > MOTOR2ANTIHORARIO_X and x < MOTOR2ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR2ANTIHORARIO_Y and y < MOTOR2ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "3"

    # Motor 3 buttons
    elif (
        x > MOTOR3HORARIO_X and x < MOTOR3HORARIO_X + BUTTON_WIDTH and
        y > MOTOR3HORARIO_Y and y < MOTOR3HORARIO_Y + BUTTON_HEIGHT
    ):
        return "4"
    elif (
        x > MOTOR3ANTIHORARIO_X and x < MOTOR3ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR3ANTIHORARIO_Y and y < MOTOR3ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "5"

    # Motor 4 buttons
    elif (
        x > MOTOR4HORARIO_X and x < MOTOR4HORARIO_X + BUTTON_WIDTH and
        y > MOTOR4HORARIO_Y and y < MOTOR4HORARIO_Y + BUTTON_HEIGHT
    ):
        return "6"
    elif (
        x > MOTOR4ANTIHORARIO_X and x < MOTOR4ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR4ANTIHORARIO_Y and y < MOTOR4ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "7"

    # Motor 5 buttons
    elif (
        x > MOTOR5HORARIO_X and x < MOTOR5HORARIO_X + BUTTON_WIDTH and
        y > MOTOR5HORARIO_Y and y < MOTOR5HORARIO_Y + BUTTON_HEIGHT
    ):
        return "8"
    elif (
        x > MOTOR5ANTIHORARIO_X and x < MOTOR5ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR5ANTIHORARIO_Y and y < MOTOR5ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "9"
