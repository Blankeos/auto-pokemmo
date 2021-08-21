import pydirectinput as pd
import time


def move(directionKey, steps):
    """
    1 step is 2 in-game steps
    """
    for i in range(steps):
        pd.press(directionKey)


def countdown():
    # print("Walking will start in:")
    # print("3")
    time.sleep(0.5)
    # print("2")
    time.sleep(0.5)
    # print("1")
    # print("Script started!")


def moveLeftAndRight():
    while True:
        move("left", 3)
        move("right", 3)


def run():
    countdown()
    moveLeftAndRight()
