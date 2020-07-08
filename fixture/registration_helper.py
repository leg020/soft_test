import time


class RegistrationHelper:

    def __init__(self, transport, scaner):
        self.app = transport
        self.scaner = scaner

    def open_registration_menu(self):
        self.app.click_element(window_name='Супервизор', button_name='Регистрация...')

    def add_mark(self, need_mark, mark):
        if need_mark == True:
            if mark != None:
                self.scaner.add_mark(mark=mark)
            else:
                self.app.click_element(window_name='Ввод штрихкода маркировки', button_name='ШК отсутствует')
                self.app.click_button('~')

    def enter_position(self, place_position, count, need_mark, mark):
        i = 1
        self.app.click_button('{F6}')
        while i < place_position:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')
        self.add_mark(need_mark=need_mark, mark=mark)
        if mark == None:
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

    def add_sale(self, need):
        if need == True:
            self.app.click_button('^ 5')