import os
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FOLDER_FOR_DATA = os.path.join(BASE_DIR, "data")

os.makedirs(FOLDER_FOR_DATA, exist_ok=True)

DATA_FILE = os.path.join(FOLDER_FOR_DATA, "library.db")

def save_database(library):
    connection = sqlite3.connect(DATA_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            year INTEGER,
            status TEXT,
            date_added TEXT
        )
    """)

    for book in library:
        cursor.execute("""
            INSERT INTO books
            (id, title, author, genre, year, status, date_added)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
        book["id"],
        book["title"],
        book["author"],
        book["genre"],
        book["year"],
        book["status"],
        book["date_added"],
    ))

    connection.commit()

    connection.close()

    print("\nLibrary Exported.")
    



def load_database():
    connection = sqlite3.connect(DATA_FILE)

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")

    rows = cursor.fetchall()

    books = []

    for row in rows:
        book = {
            "id": row["id"],
            "title": row["title"],
            "author": row["author"],
            "genre": row["genre"],
            "year": row["year"],
            "status": row["status"],
            "date_created": row["date_added"]
        }

        books.append(book)
    
    connection.close()

    return books

def initialize_database():
    connection = sqlite3.connect(DATA_FILE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            year INTEGER,
            status TEXT,
            date_added TEXT
        )
    """)

    connection.commit()
    connection.close()