import logging
from random import randint


def valid_input(in_message, retry_message, cond):
    """
    Функция запрашивающая значение переменной пока оно не будет соответствовать условиям ввода

    :param in_message: Текст с условием
    :param retry_message: Текст повторного ввода
    :param cond: Какое условие для проверки активируем
    :return: int
    """
    print(in_message)
    flag = True
    result = 0
    while flag:
        try:
            result = input(retry_message)
            match cond:
                case 1:  # ввод n
                    if int(result) > 1:
                        result = int(result)
                        flag = False
                    else:
                        print("Данные введены неверно!")
                case 2:  # ввод k
                    if int(result) >= 1:
                        result = int(result)
                        flag = False
                    else:
                        print("Данные введены неверно!")
                case 3:  # ввод попытки
                    if 1 <= int(result) <= n:
                        result = int(result)
                        flag = False
                    else:
                        print("Данные введены неверно!")
                case 4:
                    if result.lower() == "да":
                        result = True
                        flag = False
                    elif result.lower() == "нет":
                        result = False
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

    # Игровой цикл
    game = True
    logging.info(f"Game = {game}. Entered game loop.")
    while game:
        logging.info(f"Game started.")

        n = valid_input("Введите целое число большее 1 (правую границу диапазона угадывания):", "n = ", 1)
        logging.info(f"Input n = {n}")

        k = valid_input("Введите количество попыток на угадывание (натуральное число):", "k = ", 2)
        logging.info(f"Input k = {k}")

        computer = randint(1, n)
        print("Компьютер загадал число!\n")
        logging.info(f"Randomized computer number - {computer}")

        count = 1
        win = False
        print(f"Приступим к игре! Угадайте число от 1 до {n}:")
        while count - 1 != k and not win:  # Цикл угадываний
            guess = valid_input(f"Попытка {count}. Введите число от 1 до {n}", "Ваше число - ", 3)
            logging.info(f"Input guess = {guess}")

            if guess == computer:
                win = True
                logging.info(f"Player guessed!")
            elif guess > computer:
                print("Загаданное число меньше!")
                logging.info(f"Player guess {guess} < {computer}")
            else:
                print("Загаданное число больше!")
                logging.info(f"Player guess {guess} > {computer}")

            # Следующая попытка
            count += 1

        if win:
            print("Поздравляю вы угадали число!")
        else:
            print(f"Не угадали! Число было {computer}")
        logging.info(f"Game finished.")

        game = valid_input("Хотите попробовать еще раз (да/нет)?", "Ваше решение - ", 4)
        logging.info(f"Input game = {game}")
        print()

    print("Спасибо за игру!")
    logging.info("Program ended")
