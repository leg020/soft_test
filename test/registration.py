# -*- coding: utf-8 -*-
from fixture.main import *
import os.path
import jsonpickle


class Load:

    def load_from_json(self, file):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file), 'r') as f:
            return jsonpickle.decode(f.read())

data = {
    'settings': {
        'target': 'C:\\Users\\авы\\Desktop\\frontol\\releaseCandidat\\Frontol.exe',
        'scaner_port': 'COM258',
        'scaner_boundrate': 9600,
        'have_cassa': True
    },
    'data': [{
        'check_number': 1,
        'document_type': 'registration',
        'report_type': None,
        'check_type': 1,
        'help_setting': None,
        'positions': [{
            'place_in_list': 3,
            'cout': 1,
            'need_mark': True,
            'mark': '010000000000000321ergwewefwefOo910bad92lKZPjgsH0r+BMOgm4wG0delrsXR4Qeb0njR/ljdc/sqxds/wKSzcJ/zGDNoGjRBvtMbBdN+Hh+4NQxU85Se2Uw=='
        },
        {
            'place_in_list': 3,
            'cout': 3,
            'need_mark': True,
            'mark': None}],
        'sale': False,
        'type_close': 1
    },
    {
        'check_number': 2,
        'document_type': 'registration',
        'report_type': None,
        'check_type': None,
        'help_setting': 1,
        'positions': [{
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        },
        {
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        }],
        'sale': False,
        'type_close': 1
    },
    {
        'check_number': 3,
        'document_type': 'registration',
        'report_type': None,
        'check_type': 2,
        'help_setting': 1,
        'positions': [{
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        },
        {
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        }],
        'sale': False,
        'type_close': 1
    }
    ]
}


data1 = {
    'settings': {
        'target': 'C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe',
        'scaner_port': 'COM258',
        'scaner_boundrate': 9600,
        'have_cassa': True
    },
    'data': [
    {
        'check_number': 1,
        'check_type': 12,
        'help_setting': 1,
        'positions': [{
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        },
        {
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        },
        ],
        'sale': False,
        'type_close': 1
    },
    {
        'check_number': 2,
        'check_type': 13,
        'help_setting': 2,
        'positions': [{
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        },
        {
            'place_in_list': 1,
            'cout': 3,
            'need_mark': False,
            'mark': None
        },
        ],
        'sale': False,
        'type_close': 1
    }
    ]
}



f = Load()
data = f.load_from_json(file='example.json')

main = Maining(data)

main.start_frontol()

main.make_document()

main.exit_frontol()


