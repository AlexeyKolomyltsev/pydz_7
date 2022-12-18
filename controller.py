import opers_with_csv
import opers_with_txt
import view
import os

def btn_click():

    file_path = view.choose_file()
    file_ext = os.path.splitext(file_path)[1]
    operation = view.choose_oper()


    if file_ext == '.csv':
        
        if operation == '1':
            order = opers_with_csv.find(view.value(), file_path)
            print(order)

        if operation == '2':
            order = view.differ_val()
            opers_with_csv.add_value(order, file_path)
        
        if operation == '3':
            order = opers_with_csv.change_value(view.input_change_val(), file_path)
            print(order)

        if operation == '4':
            order = opers_with_csv.delete_value(view.input_delete_val(), file_path)
            print(order)

        if operation == '5':
            new_path = view.input_new_path('.txt')
            order = opers_with_csv.convert_to_txt(file_path, new_path)

    elif file_ext == '.txt':
        if operation == '1':
            order = opers_with_txt.find(view.value(), file_path)
            print(order)

        if operation == '2':
            order = view.differ_val()
            opers_with_txt.add_value(order, file_path)

        if operation == '3':
            order = opers_with_txt.change_value(view.input_change_val(), file_path)
            print(order)
        
        if operation == '4':
            order = opers_with_txt.delete_value(view.input_delete_val(), file_path)
            print(order)