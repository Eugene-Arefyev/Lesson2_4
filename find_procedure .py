
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import os.path


migrations = 'Migrations'


def filter_files(files, mask):
    filtered = []
    for file in files:
        with open(file, "r") as f:
            if mask.lower() in f.read().lower():
                filtered.append(file)
    return filtered


def get_all_sql_files(dirpath):
    return [f"{dirpath}\\{filename}" for filename in os.listdir(dirpath) if ".sql" in filename]


def print_files(files):
    for file in files:
        print(file)


def print_files_length(files):
    print(f"Всего: {len(files)}")


files = get_all_sql_files(migrations)

while True:
    mask = input("Введите строку: ")

    files = filter_files(files, mask)

    print_files(files)
    print_files_length(files)
