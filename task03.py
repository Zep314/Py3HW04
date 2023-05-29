# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции
# - функции. Дополнительно сохраняйте все операции поступления и снятия средств
# в список.

# Напишите программу банкомат.
# - Начальная сумма равна нулю
# - Допустимые действия: пополнить, снять, выйти
# - Сумма пополнения и снятия кратны 50 у.е.
# - Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# - После каждой третей операции пополнения или снятия начисляются проценты - 3%
# - Нельзя снять больше, чем на счёте
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# - Любое действие выводит сумму денег

from datetime import datetime

PUSH_SUMM_MULTIPLE = 50
PERCENT_FOR_OPERATION = 1.5
MIN_SUMM_FOR_OPERATION = 30
MAX_SUMM_FOR_OPERATION = 600
BONUS_PERCENT = 3
COUNT_OPERATION_FOR_BONUS = 3
LUXURY_SUMM = 5_000_000
LUXURY_PERCENT = 10

def print_info():
    print("""Программа - банкомат
    Доступные команды:
    /push <number> - пополнить счет на <number> денег 
    /pop <number> - снять со счета <number> денег
    /list - показать операции по счету
    /exit - выход из программы
    """)


def push_account(money):
    global account
    global history
    try:
        if (int(money) % PUSH_SUMM_MULTIPLE == 0) and (int(money) > 0):
            account += int(money)
            history[datetime.now()] = ('Пополнение счета', money, account)
        else:
            print(f"Пополнять счет можно положительной суммой, кратной {PUSH_SUMM_MULTIPLE}")
    except ValueError:
        print("Ошибка ввода")


def pop_account(money):
    global account
    global history
    try:
        if (int(money) > 0) and ((account - money) >= 0):
            account -= int(money)
            percent_fo_operation = money * PERCENT_FOR_OPERATION
            if percent_fo_operation < MIN_SUMM_FOR_OPERATION:
                percent_fo_operation = MIN_SUMM_FOR_OPERATION
            if percent_fo_operation > MAX_SUMM_FOR_OPERATION:
                percent_fo_operation = MAX_SUMM_FOR_OPERATION
            account -= percent_fo_operation

            history[datetime.now()] = ('Списание со счета', money, account)
        else:
            print("Снимать со счета можно положительную сумму, не превышая баланса")
    except ValueError:
        print("Ошибка ввода")


def list_operations():
    global history
    for key_, value_ in history.items():
        print(f'{key_}: {value_[0]}, {value_[1]:0.2f}. Баланс: {value_[2]:0.2f}')


if __name__ == '__main__':

    print_info()
    my_exit = False
    account = 0
    history = {}

    while (not my_exit):
        print(f'Баланс счета: {account:0.2f}')
        inp = input(">>> ")
        match inp.lower().split(' ')[0]:
            case "/exit":
                my_exit = True
            case "/push":
                push_account(inp.lower().split(' ')[1])
            case "/pop":
                pop_account(inp.lower().split(' ')[1])
            case "/list":
                list_operations()
            case _:
                print('Неизвестная команда')
    print('Работа завершена')
