from fixture.application import Application
from model.settings import Settings

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


    def make_check(self, positions_list):
        for row in positions_list['positions']:
            self.app.frontol_registration.enter_position(place_position=row['place_in_list'], count=row['cout'], need_mark=row['need_mark'], mark=row['mark'])
        self.app.frontol_registration.close_check(type_pay=positions_list['type_close'])

    def registration(self):
        self.app.frontol_registration.open_registration_menu()
        for row in self.data:
            self.make_check(row)
        self.app.frontol_registration.exit()

    def exit_frontol(self):
        self.app.close_main_window()

    def report(self, id=None):
        self.app.frontol_report.open_report_menu()
        if id != None:
            self.app.frontol_report.print_report_by_id(report_id=id)
        else:
            print("Не задан ни один из типов отчета")
        self.app.frontol_report.exit_report_menu()
