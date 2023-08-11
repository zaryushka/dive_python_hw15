# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# задача про калькулятор

import argparse
import math
import logging

parser = argparse.ArgumentParser(description='калькулятор')
parser.add_argument('operation', help='выберите операцию: +, -, *, /, sin, cos, tan, log, sqrt, quit')
parser.add_argument('num1', type=float, help='первое число')
parser.add_argument('num2', type=float, nargs='?', default=None, help='второе число (только для арифметических операций)')

args = parser.parse_args()

FORMAT = '{levelname:<8} - {asctime} Записано сообщение: {message}'

logging.basicConfig(filename='work_2.log', format=FORMAT, style='{', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)



if args.operation in ['sin', 'cos', 'tan', 'log', 'sqrt']:

    if args.operation == 'sin':
        result = math.sin(args.num1)
    elif args.operation == 'cos':
        result = math.cos(args.num1)
    elif args.operation == 'tan':
        result = math.tan(args.num1)
    elif args.operation == 'log':
        try:
            result = math.log(args.num1)
        except ValueError:
            logger.error('Нельзя получить логарифм отрицательного числа')
            result = None

    elif args.operation == 'sqrt':
        try:
            result = math.sqrt(args.num1)
        except ValueError:
            logger.error('Нельзя получить корень отрицательного числа')
            result = None
    print('Результат:', result)


else:

    if args.operation == '+':
        result = args.num1 + args.num2
    elif args.operation == '-':
        result = args.num1 - args.num2
    elif args.operation == '*':
        result = args.num1 * args.num2
    elif args.operation == '/':
        try:
            result = args.num1 / args.num2
        except ZeroDivisionError:
            logger.error('Деление на ноль')
            result = None
    print('Результат:', result)



# запуск из командной строки: 
# python .\home_work_2.py sqrt 16
# python .\home_work_2.py log -16
# python .\home_work_2.py / 2 0  