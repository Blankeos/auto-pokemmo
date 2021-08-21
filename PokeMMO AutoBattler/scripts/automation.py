import pyautogui as pg
import pydirectinput as pd

import time
import multiprocessing

from scripts.state import State
from scripts.state import check_battle_state_indicator

import scripts.battle as battle
import scripts.walking as walk
# processes: state indicator < battle, walking

import atexit

current_state = State.WALKING

# state_indicator_process = multiprocessing.Process(target=state_indicator)
battle_process = None
walking_process = None


def state_indicator():
    global current_state
    walking_process = multiprocessing.Process(target=walk.run)
    walking_process.start()
    while True:
        fetched_state = check_battle_state_indicator()
        if (fetched_state == State.BATTLING and current_state == State.WALKING):
            current_state = fetched_state
            # Terminate WALKING
            walking_process.terminate()
            print("Terminated WALKING")
            # Start BATTLING
            print("Starting BATTLE")
            battle_process = multiprocessing.Process(target=battle.run)
            battle_process.start()
        elif (fetched_state == State.WALKING and current_state == State.BATTLING):
            print(
                "Battle State Indicator went missing, queuing for termination...")
            time.sleep(4)
            refetch_state = check_battle_state_indicator()
            if (refetch_state == State.WALKING):
                current_state = refetch_state
                # Terminate BATTLING
                battle_process.terminate()
                print("Terminated BATTLE")
                # Start WALKING
                print("Starting WALKING")
                walking_process = multiprocessing.Process(target=walk.run)
                walking_process.start()
    pass


def terminate_all():
    print("Terminating Everything!")
    if (battle_process != None):
        battle_process.terminate()
    if (walking_process != None):
        walking_process.terminate()
    pass


def run():
    atexit.register(terminate_all)
    state_indicator()
    # battle_process.start()
    # walking_process.start()
