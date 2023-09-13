import sqlite3

corn = sqlite3.connect('laureate.db')
c = corn.cursor()

c.execute("PRAGMA foreign_keys = ON")


CO = """
CREATE TABLE IF NOT EXISTS country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255),
    code varchar(255)
)
"""
c.execute(CO)


C = """
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255) NOT NULL UNIQUE
)
"""
c.execute(C)


L = """
CREATE TABLE IF NOT EXISTS laureate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255),
    gender varchar(255),
    born_date varchar(255),
    died_date varchar(255),
    bornCountry_id INTEGER REFERENCES country(id),
    diedCountry_id INTEGER REFERENCES country(id)
)
"""
c.execute(L)


P = """
CREATE TABLE IF NOT EXISTS prize (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    laureate_id INTEGER REFERENCES laureate(id),
    category_id INTEGER REFERENCES category(id),
    year INTEGER,
    affiliation_id INTEGER REFERENCES country(id)
)
"""
c.execute(P)
print("Tables created successfully")
corn.commit()

corn.close()
