# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime


def parse_data(data: str):
    days = ['', 'понедельник', "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"].index(data.split()[1].lower())
    month_dict = {
        "января": 1, 'февраля': 2, "марта": 3,
        "апреля": 4, 'мая': 5, "июня": 6,
        "июля": 7, 'августа': 8, "сентября": 9,
        "октября": 10, 'ноября': 11, "декабря": 12
    }
    print(days)
    parse_data = data.split()
    count_week = int(parse_data[0][0])
    year = datetime.now().year
    month = month_dict[parse_data[2]]
    first_day_month = datetime(year, month, 1)
    # print(first_day_month)
    # print(first_day_month)
    # print(first_day_month.day)
    delta_days = (days - first_day_month.weekday()) % 7 + (count_week - 1) * 7
    result = datetime(year, month, delta_days)
    return result


# text = input('Введитете дату: ')
text = '1-я четверг ноября'
print(parse_data(text))