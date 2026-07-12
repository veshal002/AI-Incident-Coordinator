import sqlite3
from pathlib import Path

class SQLiteManager:
    def __init__(self):

        db_path=Path("data/incidents.db")

        db_path.parent.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(db_path)

        self.connection.row_factory=sqlite3.Row

        self.cursor=self.connection.cursor()

    def execute(self,query,params=()):
        self.cursor.execute(query, params)

        self.connection.commit()

    def fetch_one(self,query,params=()):
        self.cursor.execute(query,params)

        return self.cursor.fetchone()
    
    def fetch_all(self,query,params=()):
        self.cursor.execute(query,params)

        return self.cursor.fetchall()
    

    def initialize(self):
        with open("app/database/schema.sql") as f:
            self.connection.executescript(f.read())

        self.connection.commit()