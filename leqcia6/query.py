from insert_values import session
from sqlalchemy import func
from create_models import Author, Book, AuthorBook


class Query:
    @staticmethod
    def find_book_with_most_pages():
        return session.query(Book).order_by(Book.pages.desc()).first()

    @staticmethod
    def avg_pages():
        return session.query(func.avg(Book.pages)).scalar()

    @staticmethod
    def find_youngest_author():
        return session.query(Author).order_by(Author.birthdate.desc()).first()

    @staticmethod
    def author_with_no_books():
        return session.query(Author).filter(~Author.books.any()).all()

    @staticmethod
    def get_bonus():
        return session.query(Author).join(AuthorBook).group_by(Author.id).having(func.count(AuthorBook.book_id) > 3).limit(5).all()



