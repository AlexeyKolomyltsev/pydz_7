import csv
import view

def find(find_value):    #Функция нахождения контакта
    with open("data_base.csv", encoding='utf-8') as data_file:
        file_reader = csv.reader(data_file, delimiter = ";")
        data = []
        for i in file_reader:
            if find_value in i:
                data.append(i)
        if len(data) == 0:
            data = 'Нет такого контакта'
    return data

def add_value(value): #Функция добавления контакта
    with open("data_base.csv", mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        file_writer.writerow(value)

def change_value(value):  #Функция изменения контакта
    with open("data_base.csv", encoding='utf-8') as data_file:
        file_reader = csv.reader(data_file, delimiter = ";")
        data_value = []
        data = []
        for i in file_reader:
            if value in i:
                data_value.append(i)
                data.append(view.differ_val())
            else:
                data.append(i)
            
        if len(data_value) == 0:
            return 'Нет такого контакта'
        else:
            with open("data_base.csv", mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
                for i in data:
                    file_writer.writerow(i)
            return 'Контакт изменен'
            
def delete_value(value):  #Функция удаления контакта
    with open("data_base.csv", encoding='utf-8') as data_file:
        file_reader = csv.reader(data_file, delimiter = ";")
        data_value = []
        data = []
        for i in file_reader:
            if value in i:
                data_value.append(i)
            else:
                data.append(i)
            
        if len(data_value) == 0:
            return 'Нет такого контакта'
        else:
            with open("data_base.csv", mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
                for i in data:
                    file_writer.writerow(i)
            return 'Контакт удален'        