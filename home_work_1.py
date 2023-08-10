# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# нахождение корней квадратного уравнения

import sys
import logging
import math

logging.basicConfig(filename='work_1.log', filemode='w', encoding='utf-8', level=logging.ERROR)

def square_root(a, b, c):

    x1 = x2 = 0
    d = b**2 - 4 * a * c

    if d > 0:
        try:

            x1 = (-b  + math.sqrt(d)) / (2*a)
            x2 = (-b  - math.sqrt(d)) / (2*a)
            return x1, x2
        
        except ZeroDivisionError as e:
            logging.error('Деление на ноль')
        return None

    elif d == 0:
        x1 = (-b)/(2*a)
        return f'x1 = x2 = {x1}'

if __name__ == '__main__':
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        print(square_root(a, b, c))
    else:
        print('Используйте ввод формата: python file_name.py a b c')

    
# запуск из командной строки: python home_work_1.py 0 2 3