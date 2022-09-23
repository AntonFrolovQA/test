import PySimpleGUI as sg


def main_window(meta):
    
    layout = [
        [sg.Text(meta, text_color='red')],
        [sg.OK(key='OK'), sg.Cancel()]
    ]

    window = sg.Window(f'path to client', layout)
    while True:
        event, values = window.read(close=True)
        # =========================
        if event == "OK":
            pass
        if event in ('Cancel', None) or event == sg.WIN_CLOSED:
            break
    window.close()