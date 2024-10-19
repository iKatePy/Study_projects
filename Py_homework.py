import cowsay
import logging
# Настройка логирования
logging.basicConfig(level=logging.INFO)
def main():
    try:
        message = input("Please, say something: ")
        cowsay.cow(message)
        logging.info("Success")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
if __name__ == "__main__":
    main()