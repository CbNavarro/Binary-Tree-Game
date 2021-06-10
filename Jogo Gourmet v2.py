import PySimpleGUI as sg
sg.theme('DarkTanBlue')

def main_window():
    layout = [
        [sg.Text('Pense em um prato que gosta')],
        [sg.Button('Ok',)],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def decision_window():
    layout = [
        [sg.Text('O prato que voce pensou e massa?', size=(50,1))],
        [sg.Button('Sim',), sg.Button('Nao',)],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def questions_window():
    layout = [
        [sg.Text('O prato que voce pensou e massa?', key='texts', size=(50,1))],
        [sg.Button('Sim'), sg.Button('Nao')],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def answer1_window():
    layout = [
        [sg.Text('Qual prato voce pensou ??')],
        [sg.Input(size=(15,0), key='food')],
        [sg.Button('Ok',), sg.Button('Cancelar')],
    ]
    return sg.Window('Jogo Gourmet', layout=layout, finalize=True, size=(300,100), element_justification='c')

def answer2_window():
    layout = [
        [sg.Text('', key='titleWindow5', size=(30,0))],
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

window1 = main_window()
window2 = decision_window()
window2.hide()
window3 = questions_window()
window3.hide()
window4 = answer1_window()
window4.hide()
window5 = answer2_window()
window5.hide()
window6 = celebration_window()
window6.hide()

class No:

    def __init__(self, valor, left = None, right = None):
        self.valor = valor
        self.left = left
        self.right = right

    def get_value(self):
        return self.valor

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
       
massa = No('lasanha')
noMassaAtual = massa
noMassaAnt = noMassaAtual

outro = No('bolo de chocolate')
noOutroAtual = outro
noOutroAnt = noOutroAtual

decision = 0

def decision1():
    global noMassaAtual
    global decision
    decision = 1
    global noMassaAnt


    if window == window3 and event == 'Sim':

        if noMassaAtual.get_left():
            noMassaAtual = noMassaAtual.get_left()
        else:
            noMassaAtual = noMassaAnt
            window3.hide()
            window6.un_hide()
        
    elif window == window3 and event == 'Nao':

        if noMassaAtual.get_right():
            noMassaAtual = noMassaAtual.get_right()

        else:

            window3.hide()
            window4.un_hide()
        
    window3["texts"].update(value='O prato que voce pensou e {}? '.format(noMassaAtual.get_value()))

def decision2():

    global decision
    decision = 2
    global noOutroAtual
    global noOutroAnt


    if window == window3 and event == 'Sim':

        if noOutroAtual.get_left():
            noOutroAtual = noOutroAtual.get_left()
        else:
            noOutroAtual = noOutroAnt
            window3.hide()
            window6.un_hide()

    elif window == window3 and event == 'Nao':

        if noOutroAtual.get_right():
            noOutroAtual = noOutroAtual.get_right()
        else:

            window3.hide()
            window4.un_hide()

    window3["texts"].update(value='O prato que voce pensou e {}? '.format(noOutroAtual.get_value()))

def set_new_product_massa(product, category):
    global noMassaAnt
    global noMassaAtual

    noProd = No(product)
    noCat = No(category)

    noMassaAtual = noCat
    noCat.set_right(noMassaAnt)
    noCat.set_left(noProd)
    noMassaAnt = noMassaAtual

    window5.hide()
    window4['food']('')
    window5['category']('')
    window1.un_hide()

def set_new_product_outro(product, category):

    global noOutroAtual
    global noOutroAnt

    noProd = No(product)
    noCat = No(category)

    noOutroAtual = noCat
    noCat.set_right(noOutroAnt)
    noCat.set_left(noProd)

    noOutroAnt = noOutroAtual

    window5.hide()
    window4['food']('')
    window5['category']('')
    window1.un_hide()


while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event == sg.WIN_CLOSED:
        break

    if window and event in (sg.WIN_CLOSED, 'Cancelar'):
        window.hide()
        window1.un_hide()

    if window == window1 and event == 'Ok':
        window1.hide()
        window2 = decision_window()

    if window == window6 and event == 'Ok':
        window6.hide()
        window1.un_hide()
        
    if window == window2 and event == 'Sim':
        window2.hide()
        window3.un_hide()
        decision1()
    elif window == window2 and event == 'Nao':
        window2.hide()
        window3.un_hide()
        decision2()

    if window == window3 and event == 'Sim':
        window3.un_hide()
        if decision == 1:
            decision1()
        elif decision == 2:
            decision2()
    elif window == window3 and event == 'Nao':
        window3.un_hide()
        if decision == 1:
            decision1()
        elif decision == 2:
            decision2()
    
    if window == window4 and event == 'Ok':
        product = window4['food'].get()
        if not product:
            sg.popup("Campo Vazio", 'Conta ai em qual prato voce pensou :)')
        else:
            window4.hide()
            if decision == 1:
                window5["titleWindow5"].update(value='{} e _____ mas {} nao.'.format(product, noMassaAtual.get_value()))
            elif decision == 2:
                window5["titleWindow5"].update(value='{} e _____ mas {} nao.'.format(product, noOutroAtual.get_value()))

            window5.un_hide()

    if window == window5 and event == 'Ok':
        category = window5['category'].get()
        if not category:
            sg.popup("Campo Vazio")
        else:
            if decision == 1:
                set_new_product_massa(product, category)
            elif decision == 2:
                set_new_product_outro(product, category)