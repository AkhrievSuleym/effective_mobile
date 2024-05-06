from opportunities import *

if __name__ == "__main__":
    balance = 0 # баланс кошелька
    expenses = 0 # расходы
    income = 0 # доходы
    last_id = 0 # идентификатор последней записи
    records = [] # список для хранения записей

    records, balance, income, expenses, last_id = read_from_file('records.txt', balance, income, expenses, last_id)
    while True:
        print("Выберите действие:\n"
              "1. Вывод баланса\n"
              "2. Добавить запись\n"
              "3. Редактировать запись\n"
              "4. Поиск записей\n"
              "0. Выход\n")

        option = int(input("Введите номер действия: "))
        match option:
            case 1:
                print(f"Баланс: {balance}\n"
                      f"Доход: {income}\n"
                      f"Расход: {expenses}\n")
            case 2:
                last_id += 1
                records, balance, income, expenses = add_record(records, balance, income, expenses, last_id, 'records.txt')
            case 3:
                edit_record_id = int(input("Введите ID записи, которую вы хотите редатактировать: "))
                if edit_record_id > last_id or edit_record_id < 1:
                    print('Записи с таким ID не существует!')
                else:
                    records, balance, income, expenses = edit_record(records, balance, income, expenses, 'records.txt', edit_record_id-1)
            case 4:
                print("Выберите атрибут, по которому хотите найти записи(Дата, Категория, Сумма) ")
                attribute = input("Введите атрибут: ")
                find_record(records, attribute)
            case 0:
                exit()