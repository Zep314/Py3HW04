# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую
# словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление.


def dict_swap(local_dict):
    """
    Меняем ключ и значение местами в словаре
    Ключи становятся значениями, а значения - ключами
    :param local_dict:
    :return:
    """
    return dict(zip(local_dict.values(), local_dict.keys()))


if __name__ == '__main__':
    my_dict = {
        'ww': 333,
        1: 'qwe',
        'qqq': 'asd',
        (1, 2): 'zxc'
    }

    print(my_dict)
    print(dict_swap(my_dict))

# Результат работы
# /home/user/Work/Python/dz3/Py3HW04/venv/bin/python /home/user/Work/Python/dz3/Py3HW04/task02.py
# {'ww': 333, 1: 'qwe', 'qqq': 'asd', (1, 2): 'zxc'}
# {333: 'ww', 'qwe': 1, 'asd': 'qqq', 'zxc': (1, 2)}
#
# Process finished with exit code 0
