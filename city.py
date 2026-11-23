import sqlite3 
import pandas as pd

conn = sqlite3.connect('cities.db')

conn.execute('DROP TABLE IF NOT EXISTS CITY;')

conn.execute("""
CREATE TABLE City(
    City_Id    INTEGER  PRIMARY KEY,
    City_name  TEXT     NOT NULL UNIQUE,
    Country    TEXT     NOT NULL,
    Population INTEGER,
    Is_Capital TEXT     DEFAULT 'No' 
);""")
conn.commit()

# full row insert all columns provided
conn.execute("INSERT INTO City VALUES"
    (1, 'Tokyo', 'Japan', 13960000, 'Yes');")

    
