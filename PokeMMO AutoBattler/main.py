import time
import multiprocessing
from pynput import keyboard as kb


def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping...")


if __name__ == '__main__':

    start = time.perf_counter()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

# # Threads
# import automation

# # States
# programIsRunning = True
# botIsRunning = True


# def on_press(key):
#     global programIsRunning
#     global botIsRunning

#     if key == kb.Key.esc:
#         print("Program is terminating...")
#         programIsRunning = False
#         return False
#     elif key == kb.KeyCode.from_char("s"):
#         botIsRunning = True
#     elif key == kb.KeyCode.from_char("p"):
#         botIsRunning = False


# def the_thread():
#     global programIsRunning
#     global botIsRunning
#     while programIsRunning:
#         while not botIsRunning and programIsRunning:
#             time.sleep(0)
#         if not programIsRunning:
#             break
#         automation.run()

# # Main Automation Thread
# my_thread = threading.Thread(target=the_thread)
# my_thread.start()

# # Input Thread (Collects Keyboard Events)
# input_thread = kb.Listener(on_press=on_press)
# input_thread.start()

# # Join the threads to make them block
# my_thread.join()
# input_thread.join()
