import PySimpleGUI as sg
from Node import Node
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

window1 = main_window()
window2 = questions_window()
window2.hide()
window3 = answer1_window()
window3.hide()
window4 = answer2_window()
window4.hide()
window5 = celebration_window()
window5.hide()
       
root_node = Node('massa',Node('bolo de chocolate'),Node('lasanha'))
current_node = root_node

def create_node(new_food_type, new_food_plate):
    global current_node
    left_value = current_node.value

    current_node.value = new_food_type
    current_node.right = Node(new_food_plate)
    current_node.left = Node(left_value)

    reset_current_node()
    window4.hide()
    window3['food']('')
    window4['category']('')
    window1.un_hide()

def reset_current_node():
        global current_node
        current_node = root_node

def main():
    global current_node

    if window == window2 and event == 'Sim':

        if current_node.right or current_node.left:
            current_node = current_node.right
        else:
            window2.hide()
            window5.un_hide()
            reset_current_node()
        
    elif window == window2 and event == 'Não':

        if current_node.right or current_node.left:
            current_node = current_node.left
        else:
            window2.hide()
            window3.un_hide()
        
    window2["questions"].update(value='O prato que você pensou é {}?'.format(current_node.value))

while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event == sg.WIN_CLOSED:
        break

    if window and event in (sg.WIN_CLOSED, 'Cancelar'):
        window.hide()
        window1.un_hide()

    if window == window1 and event == 'Ok':
        window1.hide()
        window2["questions"].update(value='O prato que você pensou é {}?'.format(current_node.value))
        window2.un_hide()

    if window == window2 and event == 'Sim':
        window2.un_hide()
        main()

    elif window == window2 and event == 'Não':
        window2.un_hide()
        main()

    if window == window3 and event == 'Ok':
        product = window3['food'].get()
        if not product:
            sg.popup("Campo Vazio", 'Conta aí em qual prato você pensou :)')
        else:
            window3.hide()
            window4.un_hide()
            window4["title"].update(value='{} é _____ mas {} Não.'.format(product, current_node.value))

    if window == window4 and event == 'Ok': 
        category = window4['category'].get()
        if not category:
            sg.popup("Campo Vazio")
        else:
            create_node(category, product)

    if window == window5 and event == 'Ok':
        window5.hide()
        window1.un_hide()