import os
import sqlite3
from random import randint
from faker import Faker

fake = Faker(['en-US'])


DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'db.sqlite3')


def generate_customers(count=0):
    for _ in range(count):
        first_name = fake.first_name()
        yield [first_name]


def init_database():
    with sqlite3.connect(DEFAULT_PATH) as conn:
        with conn as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS customers 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(42) NOT NULL)"""
            )
            for customer in generate_customers(500):
                cursor.execute(
                    """INSERT INTO customers(first_name) VALUES (?)""",
                    customer
                )


def exec_query(*kwrd):
    with sqlite3.connect(DEFAULT_PATH) as conn:
        with conn as cursor:
            qs = cursor.execute(kwrd)
            results = qs.fetchall()
    return results


if __name__ == "__main__":
    init_database()