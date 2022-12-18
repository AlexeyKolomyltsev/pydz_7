import os
path = 'data_files' 

def choose_file():
    global path
    files = os.listdir(path)
    nums = list(enumerate(files, 0))
    while (id_file := int(input(f"Выберите файл данных {nums} "))) not in list(range(len(files))):
        print(f"Диапазон {list(range(len(files)))}")
    path += os.sep + files[id_file]
    return path

def choose_oper():
    while (oper:=
    input('Выберите операцию с контактом: 1-Найти 2-Добавить, 3-Изменить, 4-Удалить ')) not in ('1', '2', '3', '4'):
        print('Нет такой операции')
    return oper

def value():
    value = input("введите фамилию или номер ").capitalize()
    return value

def differ_val():
    value = list(map(str.capitalize, input("введите фамилию, имя, номер через пробел ").split()))
    return value

def input_change_val():
    value = input("введите фамилию или номер контакта, который необходимо изменить ").capitalize()
    return value

def input_delete_val():
    value = input("введите фамилию или номер контакта, который необходимо удалить ").capitalize()
    return value

