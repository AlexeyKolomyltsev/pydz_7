def choose_oper():
    while (oper:=
    input('Выберите операцию с контактом: 1-Найти 2-Добавить, 3-Изменить, 4-Удалить ')) not in ('1', '2', '3', '4'):
        print('Нет такой операции')
    return oper

def value():
    value = input("введите фамилию или номер ")
    return value

def differ_val():
    value = input("введите фамилию, имя, номер через пробел ").split()
    return value

def input_change_val():
    value = input("введите фамилию или номер контакта, который необходимо изменить ")
    return value

def input_delete_val():
    value = input("введите фамилию или номер контакта, который необходимо удалить ")
    return value