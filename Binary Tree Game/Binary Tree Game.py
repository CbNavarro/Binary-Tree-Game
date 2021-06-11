import Windows
from Node import Node

window1 = Windows.main_window()
window2 = Windows.questions_window()
window2.hide()
window3 = Windows.answer1_window()
window3.hide()
window4 = Windows.answer2_window()
window4.hide()
window5 = Windows.celebration_window()
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
    window, event, values = Windows.sg.read_all_windows()

    if window == window1 and event == Windows.sg.WIN_CLOSED:
        break

    if window and event in (Windows.sg.WIN_CLOSED, 'Cancelar'):
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
            Windows.sg.popup("Campo Vazio", 'Conta aí em qual prato você pensou :)')
        else:
            window3.hide()
            window4.un_hide()
            window4["title"].update(value='{} é _____ mas {} Não.'.format(product, current_node.value))

    if window == window4 and event == 'Ok': 
        category = window4['category'].get()
        if not category:
            Windows.sg.popup("Campo Vazio")
        else:
            create_node(category, product)

    if window == window5 and event == 'Ok':
        window5.hide()
        window1.un_hide()