import pyautogui as pg
import pydirectinput as pd

import time
import threading

from scripts.state import State
from scripts.state import check_walk_state_indicator

import scripts.battle as battle
import scripts.walking as walk

# Store the process here (must implement the interface run())
current_state_process = None


def state_check():
    global current_state_process
    while True:
        current_state = check_walk_state_indicator()
        print(current_state)
        if (current_state == State.WALKING):
            current_state_process = walk
        elif (current_state == State.BATTLING):
            current_state_process = battle


def other():
    global current_state_process
    while True:
        if (current_state_process != None):
            current_state_process.run()


state_check_process = None
other_process = None


def run():
    print("Automation Start!")
    state_check_process = threading.Thread(target=state_check)
    other_process = threading.Thread(target=other)

    state_check_process.start()
    other_process.start()
    other_process.join()
    state_check_process.join()
