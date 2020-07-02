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

    def close_main_window(self):
        self.app.click_element(window_name='Супервизор', button_name='Выход в ОС')
        self.app.click_button('~')

    def open_registration_menu(self):
        self.app.click_element(window_name='Супервизор', button_name='Регистрация...')

    def enter_position(self, place_position, count):
        i = 1
        self.app.click_button('{F6}')
        while i < place_position:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')
        i = 1
        while i < count:
            self.app.click_button('{UP}')
            i = i + 1
        self.app.click_button('~')
        self.app.click_button('{ESC}')

    def close_check(self, type_pay: int):
        i = 1
        self.app.click_button('~')
        self.app.click_button('~')
        while i < type_pay:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')
        self.app.click_button('^ {F2}')
        time.sleep(2)

    def exit(self):
        self.app.click_button('{ESC}')
        self.app.click_button('~')

    def make_check(self, positions_list):
        for row in positions_list['positions']:
            self.enter_position(place_position=row['place_in_list'], count=row['cout'])
        self.close_check(type_pay=positions_list['type_close'])

    def registration(self, positions_list):
        self.open_registration_menu()
        for row in positions_list:
            self.make_check(row)
        self.exit()
