import glob
import os


migrations = 'Migrations'
advanced_migrations = 'Advanced Migrations'


files1 = glob.glob(os.path.join(migrations, "*.sql"))
files2 = glob.glob(os.path.join(advanced_migrations, "*.sql"))


def create_files_list(list1, list2):
    result = list(list1)
    for file in list2:
        result.append(file)
    return result


def find_str(list_in, search):
    print('Всего: ', len(list_in))
    found = []
    for file_name in list_in:
        with open(file_name, encoding='utf-8', errors='ignore') as f:
            data = f.read()
            row = data.find(search)
            if row != -1:
                found.append(file_name)
    return found


def show_files_with_string(found, search):
    print('\nСписок файлов, в которых есть строка {}:'.format(search))
    for file_name in found:
        print(file_name)
    print('Всего: {0} файл(-а)'.format(len(found)))


i = 1



while True:
    if i == 1:
        files_list = create_files_list(files1, files2)

    search_line = input('\nНачинаем поиск. \nВведите строку: ')

    files_with_str = find_str(files_list, search_line)

    show_files_with_string(files_with_str, search_line)

    files_list = files_with_str[:]

    i += 1
