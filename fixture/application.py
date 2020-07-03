from fixture.frontol_reg import FrontolReg
from model.settings import Settings

class Application:

    def __init__(self, data):
        self.settings = Settings(target=data['settings']['target'],
                                 scaner_port=data['settings']['scaner_port'],
                                 scaner_boundrate=data['settings']['scaner_boundrate'],
                                 have_cassa=data['settings']['have_cassa'])
        self.data = data['data']
        self.app = None

    def start_frontol(self):
        try:
            self.app = FrontolReg(target=self.settings.target,
                                  scaner_port=self.settings.scaner_port,
                                  scaner_boundrate=self.settings.scaner_boundrate)
            self.app.open_main_window(have_cassa=self.settings.have_cassa)
        except:
            print('Ошибка при инициализации')


    def make_check(self, positions_list):
        for row in positions_list['positions']:
            self.app.enter_position(place_position=row['place_in_list'], count=row['cout'], need_mark=row['need_mark'], mark=row['mark'])
        self.app.close_check(type_pay=positions_list['type_close'])

    def registration(self):
        self.app.open_registration_menu()
        for row in self.data:
            self.make_check(row)
        self.app.exit()

    def exit_frontol(self):
        self.app.close_main_window()
