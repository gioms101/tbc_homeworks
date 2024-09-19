from faker import Faker
import sqlite3
import random
from datetime import datetime


fake = Faker()
conn = sqlite3.connect("demo.db")
c = conn.cursor()


def create_tables():
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY,
                    first TEXT,
                    last TEXT,
                    birthdate TEXT,
                    birthplace TEXT
                     )
                  """)
        c.execute("""CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    category TEXT,
                    pages INTEGER,
                    publish_date TEXT,
                    author_id INTEGER
                    )
                  """)
    insert_authors_into_table()

def insert_authors_into_table():
    with conn:
        authors = [(
            i,
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(minimum_age=35).isoformat(),
            fake.city()
            )
            for i in range(1, 501)
        ]
        c.executemany("INSERT INTO authors VALUES (?,?,?,?,?)", authors)
    insert_books_into_table()


def insert_books_into_table():
    with conn:
        genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'Non-fiction', 'Romance', 'Horror', 'Historical',
                  'Biography', 'Poetry']
        books = [
            (
                i,
                fake.sentence(),
                random.choice(genres),
                random.randint(50, 600),
                fake.date_between(start_date=datetime.strptime("00/01/01", '%y/%m/%d')),
                random.randint(1,500)
            )
            for i in range(1,1001)
        ]
        c.executemany("INSERT INTO books VALUES (?,?,?,?,?,?)", books)


# იპოვეთ და დაბეჭდეთ ყველაზე მეტი გვერდების მქონე წიგნის ყველა ველი


def find_most_page_book():
    c.execute("SELECT * FROM books WHERE pages = (SELECT MAX(pages) from books)")
    return c.fetchall()

# იპოვეთ და დაბეჭდეთ წიგნების საშუალო გვერდების რაოდენობა


def avg_pages():
    c.execute("SELECT AVG(pages) FROM books")
    return c.fetchone()

# დაბეჭდეთ ყველაზე ახალგაზრდა ავტორი


def find_youngest_author():
    c.execute("SELECT first, last, MAX(birthdate) FROM authors")
    return c.fetchall()

# დაბეჭდეთ ისეთი ავტორები რომელსაც ჯერ წიგნი არ აქვს


def author_with_no_books():
    c.execute("SELECT * FROM authors WHERE id NOT IN (SELECT author_id FROM books)")
    return c.fetchall()


# ბონუს დავალება:
# იპოვეთ ისეთი 5 ავტორი რომელსაც 3 ზე მეტი წიგნი აქვს

def get_bonus():
    c.execute("""SELECT * FROM authors WHERE id IN 
                (SELECT author_id FROM books GROUP BY author_id HAVING COUNT(author_id) > 3) LIMIT 5""")

    return c.fetchall()



if __name__ == '__main__':
    # create_tables()

    # print(find_most_page_book())
    # print(avg_pages())
    # print(find_youngest_author())
    # print(author_with_no_books())
    # print(get_bonus())
    conn.close()