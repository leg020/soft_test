from fixture.frontol_window import FrontolWindow


app = FrontolWindow(target='C:\\Program Files (x86)\\ATOL\\Frontol6\\BIN\\Frontol.exe')
app.open_main_window(have_cassa=False)
app.registration()