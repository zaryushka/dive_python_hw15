# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging

logging.basicConfig(filename='project2.log.', filemode='w', encoding='utf-8', level=logging.INFO)
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


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         data = {
#             'args': args,
#             'kwargs': kwargs,
#             'result': result
#         }
#         logging.info(data)
#         return result
#     return wrapper



@decorator
def add_nums(num1, num2, *args, **kwargs):

    return num1 + num2



if __name__ == '__main__':

    result = add_nums(54, 45, 7, 1, x = False, www = True, z = 'stroka', y = 145)

    print(result)