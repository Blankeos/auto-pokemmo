import pydirectinput as pd
import time


def countdown():
    # print("Battle starting in:")
    # print("3")
    time.sleep(0.5)
    # print("2")
    time.sleep(0.5)
    # print("1")
    # print("Script started!")


def press_a():
    while True:
        pd.press('z')
        time.sleep(0.05)


def run():
    countdown()
    pd.press('left')
    pd.press('up')
    time.sleep(0.5)
    press_a()
