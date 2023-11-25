import logging
from random import randint


def valid_input(in_message, retry_message, cond=False):
    print(in_message)
    flag = True
    result = 0
    while flag:
        try:
            result = int(input(retry_message))
            if cond:
                if result >= 1:
                    flag = False
                else:
                    print("Данные введены неверно!")
            else:
                if result > 1:
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

    n = valid_input("Введите целое число большее 1 (правую границу диапазона угадывания):", "n = ")
    logging.info(f"Input n = {n}")

    k = valid_input("Введите количество попыток на угадывание (натуральное число):", "k = ", True)
    logging.info(f"Input k = {k}")

    logging.info("Program ended")
