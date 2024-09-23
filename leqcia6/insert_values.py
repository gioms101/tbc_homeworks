from create_models import engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from create_models import Author, Book
import random


Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()


def insert_authors_books_into_table():
    genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'Non-fiction', 'Romance', 'Horror', 'Historical',
              'Biography', 'Poetry']

    books = [
        Book(
            title=fake.text(max_nb_chars=12),
            category=random.choice(genres),
            pages=random.randint(50, 600),
            publish_date=fake.date_of_birth(maximum_age=25),

        )
        for _ in range(1000)
    ]
    session.add_all(books)
    session.commit()

    authors = [
            Author(
                first=fake.first_name(),
                last=fake.last_name(),
                birthdate=fake.date_of_birth(minimum_age=35),
                birthplace=fake.city(),
                books=random.sample(books, random.randint(0,4))
            )
            for _ in range(500)
            ]
    session.add_all(authors)
    session.commit()


def insert_values_into_table():
    insert_authors_books_into_table()
