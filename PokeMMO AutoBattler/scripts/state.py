from PIL.ImageOps import grayscale
import pyautogui as pg
from enum import Enum


class State(Enum):
    WALKING = 1
    BATTLING = 2


imageRefs = ["images/player_faceleft.png", "images/player_faceright.png"]

# Better (Checks the player, not the Battle GUI)


def check_walk_state_indicator():
    """
    Checks the screen if the player is present
    Returns the State (BATTLING, WALKING)
    """
    player_imgs = []
    try:
        for imageRef in imageRefs:
            location = pg.locateOnScreen(
                imageRef, confidence=0.95, grayscale=True)
            player_imgs.append(location)

        if (player_imgs.count(None) < 2):
            return State.WALKING
        return State.BATTLING
    except:
        print("Failed to fetch image")
    return None


# Not used
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
