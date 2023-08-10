# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import sys
import random
import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" функция "{funcName}()" в {created} записала сообщение: {message}'

logging.basicConfig(filename='work_3.log.', format=FORMAT, style='{', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

glasn = 'AEIOU'
letters = 'AEIOUBCDFGHJKLMNPQRSTVWXYZ'


def gen_names(file_name, num_names):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range (num_names):
            name_len = random.randint(4, 7)
            name_1 = random.choice(glasn)
            for _ in range(name_len - 1):
                name_1 += random.choice(letters)
            stroka = f'{name_1.capitalize()}\n'
            f.write(stroka)
            logger.info(stroka)

# gen_names('words.txt', 10)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        gen_names(sys.argv[1], int(sys.argv[2]))
    else:
        print('Используйте ввод формата: python file_name.py file_name num_names')


# запуск из командной строки: python .\home_work_3.py words.txt 10