from PIL.ImageOps import grayscale
import pyautogui as pg
from enum import Enum


class State(Enum):
    WALKING = 1
    BATTLING = 2


def check_battle_state_indicator():
    """
    Checks the screen for the battle_state_indicator.png.
    Returns the State
    """
    battle_state_indicator_png = None
    try:
        battle_state_indicator_png = pg.locateOnScreen(
            "images/battle_state_indicator.png", confidence=0.95, grayscale=True)
        if (battle_state_indicator_png != None):
            return State.BATTLING
        return State.WALKING
    except:
        print("Failed to fetch battle_state_indicator_png")
    return None
