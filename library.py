import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory;')

conn.execute("""CREATE TABLE author (
    author_id   INTEGER PRIMARY KEY,
    author_name TEXT WILL NOT NULL UNIQUE 
)""")

conn.execute("""CREATE TABLE book(
    book_id     INTEGER PRIMARY KEY
    book_title  TEXT NOT NULL,
    aurthor_id  INTEGER
)""")

conn.executemany("INSERT INTO author VALUES (?, ?)",[
    (1, 'Roald Dahl'),
    (2, 'J.K Rowling'),
    (3, 'Rick Riordan'),
    (4, 'Jeff Kinney'),
    (5, 'Dav Pilkey'),
    (6, 'Lemony Snicket'),
])

conn.executemany("INSERT INTO book VALUES (?, ?, ?)",[
    (1, 'Charlie and the chocolate Factory',       1),
    (2, 'James and The Giant Peach',               1),
    (3, 'Harry Potter And The Philosophe Stone',   2),
    (4, 'Harry Potter And the Chamber of Secrets', 2),
    (5, 'The Lightning Thief',                     3),
    (6, 'The Sea of Monsters',                     3),
    (7, 'Diary of a Wimpy kid',                    4),
])

conn.commit()
