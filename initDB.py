from genericpath import exists
import sqlite3

connection = sqlite3.connect("projects.db")
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE inventory(
        name INT,
        stock INT
    );
""")
cursor.execute("""
    CREATE TABLE history(
        datetime TEXT,
        transactionValue INT,
        method TEXT,
        note TEXT
    );
""")
cursor.execute("""
    CREATE TABLE temp(
        temp INT
    );
""")
cursor.execute("""
    INSERT INTO inventory (name, stock) VALUES 
        (1,0),
        (2,0),
        (3,0),
        (4,0),
        (5,0),
        (6,0),
        (7,0),
        (8,0),
        (9,0),
        (10,0),
        (11,0),
        (12,0);
""")
cursor.execute("""
    INSERT INTO temp (temp) VALUES
        (NULL);
""")
connection.commit()