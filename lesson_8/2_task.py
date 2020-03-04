#  Retry decorator
# Предположим что у нам нужно скачать страничку из сети. Нужно реализовать декоратор,
# который будет делать указанное число попыток скачать страницу.
# Страница для теста: https://httpbin.org/status/{status}
# Коды ответа:
# 200 - Success
# 300 - Redirection
# 403, 404 - Client Errors
# 500 - Server Errors
#
# Написать функцию которая будет делать запрос с указанным нами кодом ответа. Код ответа выбираем случайно из списка.
# Сделать декоратор который будет обрабатывать коды ответа на запрос и если Х раз не удалось получить 200,
# то возвращать текст с ошибкой, иначе ОК.
import requests
import random

RCODES = [200, 300, 403, 404, 500]
URL = 'https://httpbin.org/status/{st}'


def retry(try_count):
    def create_retry(func):
        def wrapper(*args):
            counter = 0
            counter_200 = 0
            while counter != try_count:
                counter += 1
                base = func(*args)
                if base == 200:
                    print('{} - Success'.format(base))
                    counter_200 += 1
                elif base == 300:
                    print('{} - Redirection'.format(base))
                elif base == 403 or 404:
                    print('{} - Client Errors'.format(base))
                elif base == 500:
                    print('{} - Server Errors'.format(base))
            if counter_200 < try_count:
                return 'Error'
            else:
                return 'OK'
        return wrapper
    return create_retry


@retry(5)
def get_request():
    code = random.choice(RCODES)
    resp = requests.get(URL.format(st=code))
    return resp.status_code


print(get_request())
