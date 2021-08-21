import multiprocessing
from pynput import keyboard as kb
import scripts.automation as automation

# Automation Process
automation_process = multiprocessing.Process(target=automation.run)

# Input Listener Process


def on_press(key):
    if key == kb.Key.esc:
        automation_process.terminate()
        print("Program is terminating...")
        return False
    elif key == kb.KeyCode.from_char("s"):
        print("Pressed s")
    elif key == kb.KeyCode.from_char("p"):
        print("Pressed p")


input_thread = kb.Listener(on_press=on_press)

# Main


def main():
    automation_process.start()
    input_thread.start()
    automation_process.join()
    input_thread.join()
    pass


if __name__ == '__main__':
    main()
