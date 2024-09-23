import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///demo.db')
Base = sqlalchemy.orm.declarative_base()


class AuthorBook(Base):
    __tablename__ = 'authors_books'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    book_id = Column(Integer, ForeignKey("books.id"))


class Author(Base):

    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    first = Column(String)
    last = Column(String)
    birthdate = Column(Date)
    birthplace = Column(String)
    books = relationship('Book', secondary='authors_books', back_populates='authors')

    def __repr__(self):
        return f"{self.first} {self.last}"


class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    pages = Column(Integer)
    publish_date = Column(Date)
    authors = relationship('Author', secondary='authors_books', back_populates='books')

    def __repr__(self):
        return f"{self.title}"


def create_tables():
    Base.metadata.create_all(engine)