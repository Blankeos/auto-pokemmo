import pyautogui as pg
import pydirectinput as pd
import time


def move(directionKey, steps):
    """
    1 step is 2 in-game steps
    """
    for i in range(steps):
        pd.press(directionKey)


def countdown():
    print("Automation will start in:")
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    print("Script started!")


def moveLeftAndRight():
    while True:
        move("left", 20)
        move("right", 20)


def run():
    countdown()
    moveLeftAndRight()
