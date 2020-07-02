from fixture.frontol_window import FrontolWindow


Ac = [{
    'check_number': 1,
    'positions': [
        {
            'place_in_list': 3,
            'cout': 3,
        },
        {
            'place_in_list': 1,
            'cout': 3,
        }
    ],
    'type_close': 1
},
{
    'check_number': 2,
    'positions': [
        {
            'place_in_list': 3,
            'cout': 3,
        },
        {
            'place_in_list': 1,
            'cout': 3,
        }
    ],
    'type_close': 1
}]


app = FrontolWindow(target='C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe')
app.open_main_window(have_cassa=True)
app.registration(Ac)
app.close_main_window()