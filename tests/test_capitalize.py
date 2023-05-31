from capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Функция работает неверно!')


if capitalize('') != '':
    raise Exception('Функция работает неверно!')


if capitalize('1k') != '1k':
    raise Exception('Функция работает неверно!')


print('Все тесты пройдены!')

