import view
# во всех случаях файл читается целиком, затем разбивается на строки

def find(find_value, path):    #Функция нахождения контакта
    with open(path, 'r', encoding='utf-8') as data_file:
        file_reader = data_file.read().split('\n')
        data = []
        for i, line in enumerate(file_reader):
             if find_value in line:
                if find_value.isdigit():
                        data.append([file_reader[i-2], file_reader[i-1], file_reader[i]])
                else: data.append([file_reader[i], file_reader[i+1], file_reader[i+2]])
        if len(data) == 0:
            data = 'Нет такого контакта'
    return data

def add_value(value, path): #Функция добавления контакта
    with open(path, "a", encoding='utf-8') as w_file:
        w_file.write('\n')
        for i in value:
            w_file.write('\n' + i)
    print('Контакт добавлен')

def change_value(value, path):  #Функция изменения контакта
    with open(path, 'r', encoding='utf-8') as data_file:
        data = data_file.read().split('\n')
        data_check = []     #переменная для проверки нахождения контакта в книге
        for i, line in enumerate(data):   #конструкция для сохранения номера строки, в котором есть искомое значеие
             if value in line:
                data_check.append(line)
                id_line = i
                if value.isdigit(): # в зависиомости от того числовое значение или буквенное, во время формирования нового файла будет
                    flag = True     # сдвигаться индекс
                else: 
                    flag = False
                    
        if len(data_check) == 0:
            return 'Нет такого контакта'

        else:
            with open(path, "w", encoding='utf-8') as w_file:
                new_strings = view.differ_val()
                if flag:
                    data[id_line-2] = new_strings[0]
                    data[id_line-1] = new_strings[1]
                    data[id_line] = new_strings[2]
                else:
                    data[id_line] = new_strings[0]
                    data[id_line+1] = new_strings[1]
                    data[id_line+2] = new_strings[2]
                w_file.write('\n'.join(data))
            return 'Контакт изменен'
        
def delete_value(value, path):  #Функция удаления контакта
    with open(path, 'r', encoding='utf-8') as data_file:
        data = data_file.read().split('\n')
        data_check = []
        for i, line in enumerate(data):
             if value in line:
                    data_check.append(i)
                    if value.isdigit():
                        data = data[:i-2] + data[i+2:]  #для удаления используются срезы
                    else: 
                        data = data[:i] + data[i+4:] 

        if len(data_check) == 0:
            return'Нет такого контакта'
        else:
            with open(path, "w", encoding='utf-8') as w_file:
                w_file.write('\n'.join(data))
            return 'Контакт удален'   