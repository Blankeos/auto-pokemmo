import pyautogui as pg
import pydirectinput as pd
import time

def move(directionKey, steps):
    """
    1 step is 2 in-game steps
    """
    for i in range(steps):
        pd.press(directionKey)

def run():
    print("Starting walker")
    while True:
        move("left", 15)
        move("right", 15)
    pass




