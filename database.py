import sqlite3


# This file implements singleton pattern for Database class that connects to database and performs required actions

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = sqlite3.connect("uni_data")
        self.connection.row_factory = dict_factory

    def get_by_id(self, table_name, id):
        query = f"SELECT * from {table_name} where id = {id}"
        cursor = self.connection.execute(query)
        return cursor.fetchone()

    def get_generic_data(self, table_name, column, value):
        query = f"SELECT * from {table_name} where {column} = '{value}'"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def get_all(self, table_name):
        query = f"SELECT * from {table_name}"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def get_by_email(self, table_name, email):
        query = f"SELECT * from {table_name} where email = '{email}'"
        cursor = self.connection.execute(query)
        return cursor.fetchone()
