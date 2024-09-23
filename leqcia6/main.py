from create_models import create_tables
from insert_values import insert_values_into_table
from query import Query
from insert_values import session


if __name__ == '__main__':
    # create_tables()
    # insert_values_into_table()

    # print(Query.find_book_with_most_pages())
    # print(Query.find_youngest_author())
    # print(Query.author_with_no_books())
    # print(Query.avg_pages())
    # print(Query.get_bonus())

    session.close()

