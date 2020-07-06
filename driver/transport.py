from pywinauto import Application as app
from pywinauto import keyboard
import time


class Transport:

    def __init__(self, address):
        self.app = app().start(address)

    def click_element(self, window_name, button_name):
        time.sleep(1)
        open_window = self.app.window(title=window_name)
        open_window.wait('visible')
        open_window.window(title=button_name).click()
        time.sleep(1)

    def click_element_by_auto_id(self, window_name, auto_id):
        time.sleep(1)
        open_window = self.app.window(title=window_name)
        open_window.wait('visible')
        open_window.window(auto_id=auto_id).click()
        time.sleep(1)

    def click_button(self, button_name):
        time.sleep(1)
        keyboard.send_keys(button_name)

    def check_window(self, window_name):
        try:
            open_window = self.app.window(title=window_name)
            open_window.wait('visible')
            return 0
        except:
            return -1


