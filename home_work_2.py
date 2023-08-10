# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# задача про калькулятор


import math
import logging

FORMAT = '{levelname:<8} - {asctime} Записано сообщение: {message}'

logging.basicConfig(filename='work_2.log', format=FORMAT, style='{', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)



class Calculator:
    def __init__(self):
        pass

    def calc(self):
        
        while True:
            # получаем выбор пользователя
            operation = input('Выберите операцию: +, -, *, /, sin, cos, tan, log, sqrt, quit: ').lower()

            if operation == 'quit':
                # выходим из цикла, если пользователь выбрал quit
                break

            if operation in ['sin', 'cos', 'tan', 'log', 'sqrt']:
                # если пользователь выбрал научную функцию
                num = float(input('Введите число: '))
                result = None

                if operation == 'sin':
                    result = math.sin(num)
                elif operation == 'cos':
                    result = math.cos(num)
                elif operation == 'tan':
                    result = math.tan(num)
                elif operation == 'log':
                    try:
                        result = math.log(num)
                    except ValueError:
                        logger.error('Нельзя получить логарифм отрицательного числа')

                elif operation == 'sqrt':
                    try:
                        result = math.sqrt(num)
                    except ValueError:
                        logger.error('Нельзя получить корень отрицательного числа')
                print('Результат:', result)


            else:
                # если пользователь выбрал арифметическую операцию
                num1 = float(input('Введите первое число: '))
                num2 = float(input('Введите второе число: '))
                result = None

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    try:
                        result = num1 / num2
                    except ZeroDivisionError:
                        logger.error('Деление на ноль')
                print('Результат:', result)

my_calc = Calculator()
my_calc.calc()

# python .\home_work_2.py  