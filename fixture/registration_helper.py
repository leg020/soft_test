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

    def close_check_come_back(self):
        self.app.click_button('~')
        self.app.click_button('~')
        self.app.click_button('^ {F2}')


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

    def exit(self, timeout=6):
        self.app.click_button('{ESC}')
        self.app.click_button('~')
        i = 0
        while i < timeout and self.app.check_window('Супервизор') != 0:
            i = i + 1
            time.sleep(1)

    def add_sale(self, need):
        if need == True:
            self.app.click_button('^ 5')

    def add_sum_vnesenie(self, count):
        i = 1
        self.app.click_button('{F6}')
        while i < count:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')
        self.app.click_button('~')
        self.app.click_button('{ESC}')
        self.app.click_button('^ {F2}')

    def come_back_type_check(self, count):
        i = 1
        self.submit_operation_by_document(id_operation=1)
        while i < count:
            self.app.click_button('{UP}')
            i = i + 1
        self.app.click_button('{ESC}')

    def submit_operation_by_document(self, id_operation):
        i = 1
        self.app.click_button('+ {F7}')
        while i < id_operation:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')

    def new_document_type(self, check_type, set_setting):
        i = 1
        j = 1
        self.submit_operation_by_document(id_operation=1)
        while i < check_type:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')
        if check_type == 2:  # Возврат продажи
            while j < set_setting:
                self.app.click_button('{DOWN}')
                j = j + 1
            self.app.click_button('~')
            if set_setting == 2:
                self.app.click_button('~')
                self.app.click_button('~')


    def new_operation(self, operation: int):
        if operation == 10 or operation == 11 or operation == 13:
            self.submit_operation_by_document(id_operation=operation)
            self.app.click_button('~')
        elif operation == 12:
            self.submit_operation_by_document(id_operation=operation)