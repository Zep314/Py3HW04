# Напишите функцию для транспонирования матрицы


def print_matrix(local_matrix):
    """
    Красиво выводим матрицу на печать
    :param local_matrix:
    :return:
    """
    for row in local_matrix:
        print(f"{''.join(str(row))}")


def transpose_matrix(local_matrix):
    """
    Возвращает транспонированную матицу
    :param local_matrix:
    :return:
    """
    return list(list(row) for row in zip(*local_matrix))


if __name__ == '__main__':
    mmatrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [-9, 10, -11, 12],
        [13, 14, 15, 16],
    ]

    print('Исходная матрица:')
    print_matrix(mmatrix)
    print('===============')
    print('Транспонированная матрица:')
    print_matrix(transpose_matrix(mmatrix))

# Результат работы:
# C:\Work\python\dz3\Py3HW04\venv\Scripts\python.exe C:/Work/python/dz3/Py3HW04/task01.py
# Исходная матрица:
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# [-9, 10, -11, 12]
# [13, 14, 15, 16]
# ===============
# Транспонированная матрица:
# [1, 5, -9, 13]
# [2, 6, 10, 14]
# [3, 7, -11, 15]
# [4, 8, 12, 16]
#
# Process finished with exit code 0
