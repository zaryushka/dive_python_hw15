# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging

FORMAT = '{levelname:<8} - {asctime} Записала сообщение: {message}'

logging.basicConfig(filename='project3.log.', format=FORMAT, style='{', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            'args': args,
            'kwargs': kwargs,
            'result': result
        }
        logger.info(f'Функция {func.__name__}, аргументы, {data}')
        return result
    return wrapper



@decorator
def add_nums(num1, num2, *args, **kwargs):

    return num1 + num2



if __name__ == '__main__':

    result = add_nums(54, 45, 7, 1, x = False, www = True, z = 'stroka', y = 145)

    print(result)
