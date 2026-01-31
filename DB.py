import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

class DB:
    def __init__(self):
        self.string = os.getenv("Connection_String")
        self.collection = os.getenv("Collection_Name")
    
    def connect(self):
        self.connection = psycopg2.connect(self.string)
        self.cursor = self.connection.cursor()

    def clear(self):
        self.cursor.execute(f"DELETE FROM {self.collection}")
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()

