import time
import threading
import pyautogui

from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode, Key

delay = 0.1
button = Button.left
start_stop_key = KeyCode(char='ü')
exit_key = KeyCode(char='ö')


class ClickMouse(threading.Thread):
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
        i = -1155
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                #pyautogui.moveTo(i, 900)
                #pyautogui.keyDown("V")
                #üpyautogui.keyDown("enter")
                time.sleep(self.delay)
                i = i + 1
                if i > -1200:
                    i = i + 10

            time.sleep(self.delay)



mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
