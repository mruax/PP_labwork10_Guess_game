import logging
from random import randint


def valid_input(in_message, retry_message, cond):
    """
    Функция запрашивающая значение переменной пока оно не будет соответствовать условиям ввода

    :param in_message: Текст с условием
    :param retry_message: Текст повторного ввода
    :param cond: Условие проверки для n/k
    :return: int
    """
    print(in_message)
    flag = True
    result = 0
    while flag:
        try:
            result = int(input(retry_message))
            match cond:
                case 1:  # ввод n
                    if result >= 1:
                        flag = False
                    else:
                        print("Данные введены неверно!")
                case 2:  # ввод k
                    if result > 1:
                        flag = False
                    else:
                        print("Данные введены неверно!")
                case 3:  # ввод попытки
                    if 1 <= result <= n:
                        flag = False
                    else:
                        print("Данные введены неверно!")
        except Exception as e:
            print("Данные введены неверно!")
            logging.error(f"Input data: {e}")
    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logs/guess.log",
                        filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    logging.info("Program started")
    print("Добро пожаловать в Угадай-ку!")

    n = valid_input("Введите целое число большее 1 (правую границу диапазона угадывания):", "n = ", 1)
    logging.info(f"Input n = {n}")

    k = valid_input("Введите количество попыток на угадывание (натуральное число):", "k = ", 2)
    logging.info(f"Input k = {k}")

    # Игровой цикл


    computer = randint(1, n)
    print("Компьютер загадал число!")
    logging.info(f"Randomized computer number - {computer}")

    count = 1
    win = False
    print(f"Приступим к игре! Угадайте число от 1 до {n}:")
    # Цикл угадываний
    while count - 1 != k:
        guess = valid_input(f"Попытка {count}. Введите число от 1 до {n}", "Ваше число - ", 3)
        logging.info(f"Input guess = {guess}")

        if guess == computer:
            count = k + 1
            win = True
        elif guess > computer:
            print("Загаданное число меньше!")
        else:
            print("Загаданное число больше!")

        # Следующая попытка
        count += 1

    if win:
        print("Поздравляю вы угадали число!")
    else:
        print("Ничего страшного, бывает!")


    logging.info("Program ended")
