__author__ = 'student'
# импортируем модуль
import sys
import os

# выводим на экран список всех аргументов
for arg in sys.argv[1:]:
    if os.path.exists(arg):
        with open(arg) as f:
            for line in f:
                print(line, end='')
        print('\n')
