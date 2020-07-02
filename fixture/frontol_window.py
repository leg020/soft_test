from fixture.application import Application
import time


class FrontolWindow:

    def __init__(self, target):

        self.app = Application(address=target)


    def open_main_window(self, have_cassa=True):

        if have_cassa == False:

            time.sleep(4)
            self.app.click_button('~')

        self.app.click_element(window_name='Авторизация доступа', button_name='ОК')
        if self.app.check_window(window_name='Супервизор') == 0:
            return 0
        else:
            return -1

    def registration(self):
        self.app.click_element(window_name='Супервизор', button_name='Регистрация...')
        self.app.click_button('{F6}')
        self.app.click_button('{DOWN}')
        self.app.click_button('~')