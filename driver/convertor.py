from model.settings import Settings
from model.data import Data
from model.positions_in_check import *

class Convertor:

    def __init__(self):
        self.err = []
        self.data = None

    def convert_positions_to_test_model(self, positions_list:[]):
        data = []
        try:
            for row in positions_list:
                data.append(PositionsInCheck(place_in_list=row['place_in_list'],
                                             cout=row['cout'],
                                             need_mark=row['need_mark'],
                                             mark=row['mark']))
            return data
        except:
            self.err.append('There is exception in positions')
            return -1

    def convert_documents_to_test_model(self, file):
        data = []
        for row in file['data']:
            positions = self.convert_positions_to_test_model(row['positions'])
            if positions != -1:
                try:
                    data.append(Checks(check_number=row['check_number'],
                                           document_type=row['document_type'],
                                           report_type=row['report_type'],
                                           check_type=row['check_type'],
                                           help_setting=row['help_setting'],
                                           type_close=row['type_close'],
                                           sale=row['sale'], positions=positions))
                except:
                    self.err.append('There is exception in documents')
                    data = -1
            else:
                data = -1
        return data



    def convert_to_test_model(self, file):
        data = self.convert_documents_to_test_model(file=file)
        if data != -1:
            try:
                self.data = Data(settings=Settings(target=file['settings']['target'],
                                                   scaner_port=file['settings']['scaner_port'],
                                                   scaner_boundrate=file['settings']['scaner_boundrate'],
                                                   have_cassa=file['settings']['have_cassa']),
                                 data=data)
                return 0
            except:
                self.err.append('There is exception')
                return -1
        else:
            return -1
