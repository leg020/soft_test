from fixture.registration_helper import RegistrationHelper
from fixture.transport import Transport
from fixture.scaner import Scaner
from fixture.report_helper import ReportHelper
import time

class Application:

    def __init__(self, target, scaner_port=None, scaner_boundrate=9600):
        self.transport = Transport(address=target)
        self.scaner = None
        if scaner_port != None:
            self.scaner = Scaner(port=scaner_port, baudrate=scaner_boundrate)

        self.frontol_registration = RegistrationHelper(transport=self.transport, scaner=self.scaner)
        self.frontol_report = ReportHelper(transport=self.transport)

    def open_main_window(self, have_cassa=True):
        if have_cassa == False:

            time.sleep(4)
            self.transport.click_button('~')

        self.transport.click_element(window_name='Авторизация доступа', button_name='ОК')
        if self.transport.check_window(window_name='Супервизор') == 0:
            return 0
        else:
            return -1

    def close_main_window(self):
        self.scaner.close_port()
        self.transport.click_element(window_name='Супервизор', button_name='Выход в ОС')
        self.transport.click_button('~')