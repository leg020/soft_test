from fixture.main import Main

#C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe

data = {
    'settings': {
        'target': 'C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe',
        'scaner_port': 'COM258',
        'scaner_boundrate': 9600,
        'have_cassa': True
    },
    'data': [{
        'check_number': 1,
        'document_type': 'registration',
        'report_type': 1,
        'check_type': None,
        'help_setting': None,
        'positions': [{
            'place_in_list': 1,
            'cout': 1,
            'need_mark': False,
            'mark': None
        },
        {
            'place_in_list': 4,
            'cout': 1,
            'need_mark': False,
            'mark': None}],
        'sale': False,
        'type_close': 1
    },
    {
        'check_number': 2,
        'document_type': 'registration',
        'report_type': None,
        'check_type': None,
        'help_setting': None,
        'positions': [{
            'place_in_list': 5,
            'cout': 1,
            'need_mark': False,
            'mark': None
        },
        {
            'place_in_list': 6,
            'cout': 1,
            'need_mark': False,
            'mark': None
        }],
        'sale': False,
        'type_close': 1
    }]
}


main = Main(data)

main.start_frontol()

main.make_document()

main.exit_frontol()