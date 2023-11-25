import logging
from random import randint


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logs/guess.log",
                        filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    logging.info("Program started")
    print("Добро пожаловать в Угадай-ку!")

    flag = True
    n = 0
    print("Введите максимальное число диапазона угадывания:")
    while flag:
        try:
            n = int(input("n = "))
            if n > 1:
                flag = False
        except Exception:
            print("Данные введены неверно! Ваше число должно быть натуральным и большим чем единица.")
            logging.error(f"Ошибка ввода данных: {Exception}")
    logging.info(f"Задано n = {n}")

    

    logging.info("Program ended")
