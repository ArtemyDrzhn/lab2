import os
import shutil

DIRECTORY = "D:/Study/University/Sem 7/КПРС ПО/Лабораторные/2/target dir"

source = os.walk(DIRECTORY)

# Переименование файлов для дальнейшего перемещения
for root, dirs, files in os.walk(DIRECTORY):
    # Пропуск корнего каталога
    if root == DIRECTORY:
        continue

    # Извлечение подстроки для переименования файлов
    path_name = (root.rpartition(DIRECTORY)[2].replace('/', '_'))

    # Переименование файлов
    for name_file in files:
        old_file = root + '/' + name_file
        new_file = DIRECTORY + path_name + '_' + name_file
        os.rename(old_file, new_file)

# Удаление каталогов
for e in os.listdir(DIRECTORY):
    full_path = f'{DIRECTORY}/{e}'
    if os.path.isdir(full_path):
        shutil.rmtree(full_path, ignore_errors=False)
