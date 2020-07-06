import time

class ReportHelper:

    def __init__(self, transport):
        self.app = transport

    def open_report_menu(self):
        self.app.click_element(window_name='Супервизор', button_name='Сервис...')

    def print_report_by_id(self, report_id):
        i = 0
        while i < report_id:
            self.app.click_button('{DOWN}')
            i = i + 1
        self.app.click_button('~')
        self.app.click_button('~')
        time.sleep(7)

    def exit_report_menu(self):
        self.app.click_button('{ESC}')

