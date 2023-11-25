import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logs/guess.log",
                        filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    logging.info("Program started")

    logging.info("Program ended")
