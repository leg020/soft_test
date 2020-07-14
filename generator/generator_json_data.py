# -*- coding: utf-8 -*-
from model.data import Data
from model.settings import Settings
from model.positions_in_check import *
import jsonpickle
import os.path


settings = Settings(target='C:\\Users\\авы\\Desktop\\frontol\\releaseCandidat\\Frontol.exe',
                    scaner_port='COM258',
                    scaner_boundrate=9600,
                    have_cassa=True)

positions = [PositionsInCheck(place_in_list=1, cout=1, need_mark=False, mark=None),
             PositionsInCheck(place_in_list=1, cout=1, need_mark=False, mark=None)]

documents = [Checks(check_number=1,
                    document_type='registration',
                    report_type=1,
                    check_type=None,
                    help_setting=None,
                    sale=False,
                    type_close=1,
                    positions=positions),
             Checks(check_number=1,
                    document_type='report',
                    report_type=7,
                    check_type=None,
                    help_setting=None,
                    sale=False,
                    type_close=1,
                    positions=positions)]

data = Data(settings=settings, data=documents)

f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example.json')
with open(f, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(data))





