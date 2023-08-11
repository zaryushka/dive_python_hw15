# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# нахождение корней квадратного уравнения

import argparse
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


parser = argparse.ArgumentParser(description='вычисление корней квадратного уравнения')
parser.add_argument('a', type=float, help='коэффициент a')
parser.add_argument('b', type=float, help='коэффициент b')
parser.add_argument('c', type=float, help='коэффициент c')

args = parser.parse_args()
result = square_root(args.a, args.b, args.c)
print(result)


    
# запуск из командной строки: python home_work_1.py 0 2 3