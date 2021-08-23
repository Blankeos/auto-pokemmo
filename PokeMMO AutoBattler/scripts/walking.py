import pydirectinput as pd
import time


def move(directionKey, steps):
    """
    1 step is 2 in-game steps
    """
    for i in range(steps):
        pd.press(directionKey)


def moveLeftAndRight():
    move("left", 3)
    move("right", 3)


def run():
    # print("WALKING")
    moveLeftAndRight()
