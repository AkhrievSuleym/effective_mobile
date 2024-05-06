from datetime import date
from parsing import *

def add_record(records, balance, income, expenses, last_id, filename):
    """
        Функция для добавления записей.
    """
    cur_date = date.today()
    category = input("Введите категорию записи(Доход/Расход): ")
    amount = int(input('Сумма: '))
    description = input('Описание: ')

    if category == "Расход":
        balance -= amount
        expenses += amount
    elif category == "Доход":
        balance += amount
        income += amount
    else:
        print("Введена неправильная категория!")
        category = input("Введите категорию записи(Доход/Расход): ")

    with open(filename, 'a') as file:
        file.write(f"ID: {last_id}\n"
                   f"Дата: {cur_date}\n"
                   f"Категория: {category}\n"
                   f"Сумма: {amount}\n"
                   f"Описание: {description}\n"
                   f"\n")
    records.append(Record(last_id, date, category, amount, description))
    print('Запись успешно добавлена')
    return records, balance, income, expenses

def edit_record(records, balance, income, expenses, filename, id):
    """
        Функция для редактирования записей по идентификатору(ID).
    """
    cur_date = date.today()
    print("Введите данные, которые хотите редактировать")
    category = input("Введите категорию записи, (Доход/Расход): ")
    amount = int(input('Сумма: '))
    description = input('Описание: ')

    records[id].date = cur_date
    if records[id].category == 'Доход':
        balance -= int(records[id].amount)
        income -= int(records[id].amount)
    else:
        balance += int(records[id].amount)
        expenses -= int(records[id].amount)

    records[id].category = category
    if category == 'Доход':
        balance += amount
        income += amount
    else:
        balance -= amount
        expenses += amount

    records[id].amount = amount
    records[id].description = description
    write_in_file(records, filename)
    print('Запись успешно отредактирована!\n')
    return records, balance, income, expenses

def find_record(records, attribute):
    """
        Функция для поиска записей по категории, дате или сумме.
        Args:
              records - список записей.
              attribute - аттрибут для поиска.
    """
    found = False
    match attribute:
        case 'Дата':
            search = input("Введите дату в формате(YYYY-MM-DD): ")
            for record in records:
                if record.date == search:
                    found = True
                    print(record)
        case 'Категория':
            search = input("Введите категорию(Доход/Расход): ")
            for record in records:
                if record.category == search:
                    found = True
                    print(record)
        case 'Сумма':
            search = int(input("Введите сумму: "))
            for record in records:
                if int(record.amount) == search:
                    found = True
                    print(record)
    if not found:
        print("По полученным данным отсутствуют записи!")
