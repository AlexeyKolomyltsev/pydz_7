import opers_with_csv
import view

def btn_click():
    operation = view.choose_oper()
    if operation == '1':
        order = opers_with_csv.find(view.value())
        print(order)

    if operation == '2':
        order = view.differ_val()
        print(order)
        opers_with_csv.add_value(order)
    
    if operation == '3':
        order = opers_with_csv.change_value(view.input_change_val())
        print(order)

    if operation == '4':
        order = opers_with_csv.delete_value(view.input_delete_val())
        print(order)