from constants import *


def button_clicked(pos):
    x, y = pos
    # Identifying button clicked
    # Motor 1 buttons
    if (
        x > MOTOR1HORARIO_X and x < MOTOR1HORARIO_X + BUTTON_WIDTH and
        y > MOTOR1HORARIO_Y and y < MOTOR1HORARIO_Y + BUTTON_HEIGHT
    ):
        return "M1H"
    elif (
        x > MOTOR1ANTIHORARIO_X and x < MOTOR1ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR1ANTIHORARIO_Y and y < MOTOR1ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "M1A"

    # Motor 2 buttons
    elif (
        x > MOTOR2HORARIO_X and x < MOTOR2HORARIO_X + BUTTON_WIDTH and
        y > MOTOR2HORARIO_Y and y < MOTOR2HORARIO_Y + BUTTON_HEIGHT
    ):
        return "M2H"
    elif (
        x > MOTOR2ANTIHORARIO_X and x < MOTOR2ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR2ANTIHORARIO_Y and y < MOTOR2ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "M2A"

    # Motor 3 buttons
    elif (
        x > MOTOR3HORARIO_X and x < MOTOR3HORARIO_X + BUTTON_WIDTH and
        y > MOTOR3HORARIO_Y and y < MOTOR3HORARIO_Y + BUTTON_HEIGHT
    ):
        return "M3H"
    elif (
        x > MOTOR3ANTIHORARIO_X and x < MOTOR3ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR3ANTIHORARIO_Y and y < MOTOR3ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "M3A"

    # Motor 4 buttons
    elif (
        x > MOTOR4HORARIO_X and x < MOTOR4HORARIO_X + BUTTON_WIDTH and
        y > MOTOR4HORARIO_Y and y < MOTOR4HORARIO_Y + BUTTON_HEIGHT
    ):
        return "M4H"
    elif (
        x > MOTOR4ANTIHORARIO_X and x < MOTOR4ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR4ANTIHORARIO_Y and y < MOTOR4ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "M4A"

    # Motor 5 buttons
    elif (
        x > MOTOR5HORARIO_X and x < MOTOR5HORARIO_X + BUTTON_WIDTH and
        y > MOTOR5HORARIO_Y and y < MOTOR5HORARIO_Y + BUTTON_HEIGHT
    ):
        return "M5H"
    elif (
        x > MOTOR5ANTIHORARIO_X and x < MOTOR5ANTIHORARIO_X + BUTTON_WIDTH and
        y > MOTOR5ANTIHORARIO_Y and y < MOTOR5ANTIHORARIO_Y + BUTTON_HEIGHT
    ):
        return "M5A"
