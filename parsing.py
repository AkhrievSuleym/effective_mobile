class Record:
    def __init__(self, ID, date, category, amount, description):
        """
            Инициализация объекта.
            Args:
              ID (int): Уникальный идентификатор записи
              date (str): Дата записи в формате YYYY-MM-DD.
              category (str): Категория записи (например, "Расход", "Доход").
              amount (float): Сумма записи.
              description (str): Описание записи.
            """
        self.ID = ID
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        """
        Представление объекта в виде строки.
        Returns:
          str: Строковое представление записи.
        """
        return f"Дата: {self.date}\nКатегория: {self.category}\nСумма: {self.amount}\nОписание: {self.description}\n"

def read_from_file(filename, balance, income, expenses, last_id):
    """
      Функция для парсинга текстового файла и создания списка записи.
    """
    records = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        part = line.split(': ')
        if part != ['\n']:
            match part[0]:
                case 'ID':
                    last_id = int(part[1][:-1])
                case 'Дата':
                    date = part[1][:-1]
                case 'Категория':
                    category = part[1][:-1]
                case 'Сумма':
                    amount = part[1][:-1]
                    if category == 'Расход':
                        balance -= int(part[1])
                        expenses += int(part[1])
                    else:
                        balance += int(part[1])
                        income += int(part[1])
                case 'Описание':
                    description = part[1][:-1]
        else:
            if last_id != 0:
                record = Record(last_id, date, category, amount, description)
                records.append(record)

    return records, balance, income, expenses, last_id

def write_in_file(records, filename):
    """
        Функция для записи в текстовый файл изменений и новых записей.
    """
    with open(filename, 'w') as file:
        for record in records:
            file.write('ID: ' + str(record.ID) + '\n')
            file.write('Дата: ' + str(record.date) + '\n')
            file.write('Категория: ' + record.category + '\n')
            file.write('Сумма: ' + str(record.amount) + '\n')
            file.write('Описание: ' + record.description + '\n')
            file.write('\n')


