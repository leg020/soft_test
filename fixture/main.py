from fixture.application import Application
from model.settings import Settings
from model.positions_in_check import Checks

class Main:

    def __init__(self, data):
        self.settings = Settings(target=data['settings']['target'],
                                 scaner_port=data['settings']['scaner_port'],
                                 scaner_boundrate=data['settings']['scaner_boundrate'],
                                 have_cassa=data['settings']['have_cassa'])
        self.data = data['data']
        self.app = None

    def start_frontol(self):
        try:
            self.app = Application(target=self.settings.target,
                                  scaner_port=self.settings.scaner_port,
                                  scaner_boundrate=self.settings.scaner_boundrate)
            self.app.open_main_window(have_cassa=self.settings.have_cassa)
        except:
            print('Ошибка при инициализации')

    def add_positions_in_check_and_close(self, check: Checks()):
        for row in check.positions:
            self.app.frontol_registration.enter_position(place_position=row['place_in_list'],
                                                         count=row['cout'],
                                                         need_mark=row['need_mark'],
                                                         mark=row['mark'])
        self.app.frontol_registration.add_sale(need=check.sale)
        self.app.frontol_registration.close_check(type_pay=check.type_close)

    def make_check(self, check):
        data = Checks()
        data.check_type = check['check_type']
        data.help_setting = check['help_setting']
        data.sale = check['sale']
        data.check_number = check['check_number']
        data.type_close = check['type_close']
        data.positions = check['positions']
        if data.check_type != None:
            self.app.frontol_registration.new_document_type(check_type=data.check_type,
                                                        set_setting=data.help_setting)
        if data.check_type == 2:
            if data.help_setting == 2:
                self.app.frontol_registration.close_check_come_back()
            else:
                self.add_positions_in_check_and_close(data)
        elif data.check_type == 3 or data.check_type == 4:
            self.app.frontol_registration.add_sum_vnesenie(3)
        else:
            self.add_positions_in_check_and_close(data)
        if data.check_type != None:
            self.app.frontol_registration.come_back_type_check(data.check_type)

    def make_document(self):
        #self.app.frontol_registration.open_registration_menu()
        for row in self.data:
            if row['document_type'] == 'registration':
                self.registration(row)
            if row['document_type'] == 'report':
                self.report(row)

    def registration(self, position):
        self.app.frontol_registration.open_registration_menu()
        self.make_check(position)
        self.app.frontol_registration.exit()

    def exit_frontol(self):
        self.app.close_main_window()

    def report(self, position):
        self.app.frontol_report.open_report_menu()
        self.app.frontol_report.print_report_by_id(report_id=position['report_type'])
        self.app.frontol_report.exit_report_menu()



class Maining:

    def __init__(self, log):
        self.settings = None
        self.data = None
        self.app = None
        self.log = log

    def set_object_data(self, data):
        self.log.add_log(type_message='INFO', message='start add data')
        self.settings = Settings(target=data.settings.target,
                                 scaner_port=data.settings.scaner_port,
                                 scaner_boundrate=data.settings.scaner_boundrate,
                                 have_cassa=data.settings.have_cassa)
        self.data = data.data
        self.app = None
        self.log.add_log(type_message='INFO', message='finish enter data')

    def start_frontol(self):
        try:
            self.log.add_log(type_message='INFO', message='start frontol')
            self.app = Application(target=self.settings.target,
                                  scaner_port=self.settings.scaner_port,
                                  scaner_boundrate=self.settings.scaner_boundrate)
            self.app.open_main_window(have_cassa=self.settings.have_cassa)
            self.log.add_log(type_message='INFO', message='finish start frontol')
        except:
            self.log.add_log(type_message='ERR', message='init mistake')

    def add_positions_in_check_and_close(self, check: Checks()):
        self.log.add_log(type_message='INFO', message='add position')
        for row in check.positions:
            self.app.frontol_registration.enter_position(place_position=row.place_in_list,
                                                         count=row.cout,
                                                         need_mark=row.need_mark,
                                                         mark=row.mark)
        self.app.frontol_registration.add_sale(need=check.sale)
        self.app.frontol_registration.close_check(type_pay=check.type_close)

    def make_check(self, check):
        self.log.add_log(type_message='INFO', message='start add check')
        data = Checks()
        data.check_type = check.check_type
        data.help_setting = check.help_setting
        data.sale = check.sale
        data.check_number = check.check_number
        data.type_close = check.type_close
        data.positions = check.positions
        if data.check_type != None:
            self.log.add_log(type_message='INFO', message='check type = None')
            self.app.frontol_registration.new_document_type(check_type=data.check_type,
                                                        set_setting=data.help_setting)
        if data.check_type == 2:
            self.log.add_log(type_message='INFO', message='check type = 2')
            if data.help_setting == 2:
                self.log.add_log(type_message='INFO', message='check type = 2 and help setting = 2')
                self.app.frontol_registration.close_check_come_back()
            else:
                self.log.add_log(type_message='INFO', message='check type = 2 and help setting = other')
                self.add_positions_in_check_and_close(data)
        elif data.check_type == 3 or data.check_type == 4:
            self.log.add_log(type_message='INFO', message='check type = 3 or 4')
            self.app.frontol_registration.add_sum_vnesenie(3)
        else:
            self.log.add_log(type_message='INFO', message='check type = other')
            self.add_positions_in_check_and_close(data)
        if data.check_type != None:
            self.log.add_log(type_message='INFO', message='come back check tipe')
            self.app.frontol_registration.come_back_type_check(data.check_type)

    def make_document(self):
        #self.app.frontol_registration.open_registration_menu()
        for row in self.data:
            if row.document_type == 'registration':
                self.log.add_log(type_message='INFO', message='document type REGISTRATION')
                self.registration(row)
            if row.document_type == 'report':
                self.log.add_log(type_message='INFO', message='document type REPORT')
                self.report(row)

    def registration(self, position):
        self.log.add_log(type_message='INFO', message='start registration')
        self.app.frontol_registration.open_registration_menu()
        self.make_check(position)
        self.app.frontol_registration.exit()

    def exit_frontol(self):
        self.log.add_log(type_message='INFO', message='exit frontol')
        self.app.close_main_window()

    def report(self, position):
        self.log.add_log(type_message='INFO', message='start report')
        self.app.frontol_report.open_report_menu()
        self.app.frontol_report.print_report_by_id(report_id=position.report_type)
        self.app.frontol_report.exit_report_menu()

    def get_log(self):
        return self.log.log_list
