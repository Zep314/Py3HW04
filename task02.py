# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую
# словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хэшируем, используйте его строковое представление.


def dict_swap(local_dict):
    """
    Меняем ключ и значение местами в словаре
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
