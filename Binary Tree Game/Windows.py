import PySimpleGUI as sg
sg.theme('DarkBlue3')

def main_window():
    layout = [
        [sg.Text('Pense em um prato que gosta…')],
        [sg.Button('Ok',)],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def questions_window():
    layout = [
        [sg.Text('O prato que você pensou é {}?', key='questions', size=(50,1))],
        [sg.Button('Sim'), sg.Button('Não')],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def answer1_window():
    layout = [
        [sg.Text('Qual prato você pensou ??')],
        [sg.Input(size=(15,0), key='food')],
        [sg.Button('Ok',), sg.Button('Cancelar')],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def answer2_window():
    layout = [
        [sg.Text('', key='title', size=(30,0))],
        [sg.Input(size=(15,0), key='category')],
        [sg.Button('Ok',), sg.Button('Cancelar')],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def celebration_window():
    layout = [
        [sg.Text('Acertei de novo!!')],
        [sg.Button('Ok',)],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')