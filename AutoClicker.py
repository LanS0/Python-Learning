from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
import threading
import time

class AutoClicker:
    def __init__(self):
        self.running = False
        self.keyboard_listener = None
        self.auto_clicker_on = False

    def start(self):
        self.running = True
        self.loop()

    def keyboard_evento(self, event):
        try:
            if event.key == keyboard.Key.esc:
                self.running = False

            if event.key.char == 's':
                self.klick_able(event.key.char)

            print(event, "HELLO", self.auto_clicker_on)

            self.mouse_clicking()
        except :            
            return

    def loop(self):
        while self.running:
            with keyboard.Events() as events:
                for event in events:
                    if isinstance(event, keyboard.Events.Press):
                        self.keyboard_evento(event)
    
                    if self.running == False:
                        break

    def klick_able(self, key):
        if self.auto_clicker_on == False:
            self.auto_clicker_on = True
        else:
            self.auto_clicker_on = False

    def mouse_clicking(self):
        print(self.auto_clicker_on)
        while self.auto_clicker_on:
            print("HELLO")

        t = threading.Thread(target=self.mouse_clicking())
        t.start()
            
mouse = Controller()
auto_clicker = AutoClicker()
auto_clicker.start()

