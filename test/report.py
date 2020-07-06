from fixture.main import Main


data = {
    'settings': {
        'target': 'C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe',
        'scaner_port': 'COM258',
        'scaner_boundrate': 9600,
        'have_cassa': True
    },
    'data': [{
        'check_number': 1,
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
        'type_close': 1
    },
    {
        'check_number': 2,
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
        'type_close': 1
    }]
}

main = Main(data)
main.start_frontol()
main.report(id=7)
main.report(id=1)
main.exit_frontol()