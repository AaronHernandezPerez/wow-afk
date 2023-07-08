import time
from threading import Thread
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener, KeyCode

from tkinter import Tk

tinker_root = Tk()

# Get the screen size
screen_height = tinker_root.winfo_screenheight()
screen_width = tinker_root.winfo_screenwidth()

# Rough estimates for the two buttons ("you have been disconnected" and "reconnect")
screen_points = {
    "dialog": [
        screen_width / 2,
        (screen_height / 2) + 24,
    ],
    "reconnect": [
        screen_width / 2,
        (screen_height / 2) + 124,
    ],
}


# to control clicks
class ClickMouse(Thread):
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = (
                    screen_points.get("dialog")[0],
                    screen_points.get("dialog")[1],
                )
                time.sleep(0.1)
                mouse.click(self.button)

                time.sleep(1)

                mouse.position = (
                    screen_points.get("reconnect")[0],
                    screen_points.get("reconnect")[1],
                )
                time.sleep(0.1)
                mouse.click(self.button)

                time.sleep(self.delay)
            time.sleep(0.1)


# Bot config
delay = 30
button = Button.left
start_stop_key = KeyCode(char="s")
stop_key = Key.esc

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    # start_stop_key will stop clicking
    # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("Stopped")
        else:
            click_thread.start_clicking()
            print("Started")

    # here exit method is called and when
    # key is pressed it terminates auto clicker
    elif key == Key.esc:
        click_thread.exit()
        listener.stop()
        print("Closing, it may take a moment")


with Listener(on_press=on_press) as listener:
    print("Press the [s] key to start/stop, to exit press the [esc] key")
    listener.join()
