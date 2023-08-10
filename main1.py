# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='project.log.', filemode='w', encoding='utf-8', level=logging.ERROR)

def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.error('Деление на ноль')
        result = None
    return result

print(div(4, 0))