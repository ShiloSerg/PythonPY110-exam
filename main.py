import json
import random
from faker import Faker
from conf import MODEL


def decorator_task_4(max_len_number: int):
    """
    Фабрика декораторов, принимает максимальную длину как параметр и
    проводит валидацию названия книги, а именно проверяет
    максимальную длину книги
    """

    def decorator_task_2(func):
        def page_validation():
            data = func()
            if len(data) > max_len_number:
                raise ValueError('Слишком много символов в названии одной из книг')
            # else:
            return data

        return page_validation

    return decorator_task_2


def main(number: int, pk: int) -> json:
    """
    Функция записи сгенерированных книг в файл.
    number: Количество копий книг, которое необходимо сгенерировать
    pk: Счетчик сгенерированных книг, по умолчанию = 1, можно поставить
    необходимое значение.
    """
    books_list = []
    book = generate_book(pk)
    for _ in range(number):
        books_list.append(next(book))
    file = "Books.json"
    with open(file, "w", encoding="utf-8") as f:
        json.dump(books_list, f, indent=4, ensure_ascii=False)


def generate_book(counter: int) -> dict:
    """
    Функция - генератор информации о книге
    """
    while True:
        book = {
            "model": MODEL,
            "pk": counter,
            "fields": {
                "title": generate_random_title(),
                "year": generate_random_year(),
                "pages": generate_random_pages(),
                "isbn13": generate_random_isbn13(),
                "rating": generate_random_rating(),
                "price": generate_random_price(),
                "author": generate_authors()
            }
        }
        yield book
        counter += 1


@decorator_task_4(45)
def generate_random_title() -> str:
    """
    Функция выбора случайной книги из файла
    """
    book = []
    with open("books.txt", encoding="utf-8") as f:
        for elem in f.readlines():
            book.append(elem.strip())
    return random.choice(book)


def generate_random_year() -> int:
    """
    Функция генерирует случайный год
    """
    year = random.randint(1900, 2022)
    return year


def generate_random_pages() -> int:
    """
    Функция генерирует случайное число страниц
    """
    pages = random.randint(100, 250)
    return pages


def generate_random_isbn13() -> str:
    """
    Функция генерирует случайный isbn13
    """
    fake = Faker()
    isbn13 = fake.isbn13()
    return isbn13


def generate_random_rating() -> float:
    """
   Функция генерирует случайный рейтинг книги, от 1 до 5
    """
    rating = random.uniform(0, 5)
    return round(rating, 1)


def generate_random_price() -> float:
    """
    Функция генерирует случайную цену
    """
    price = random.uniform(100, 5000)
    return round(price, 2)


def generate_authors() -> list:
    """
    Функция генерирует список случайных авторов
    """
    fake = Faker('ru_RU')
    list_authors = []
    for _ in range(random.randint(1, 3)):
        list_authors.append(fake.name())
    return list_authors


if __name__ == '__main__':
    main(100, 1)
