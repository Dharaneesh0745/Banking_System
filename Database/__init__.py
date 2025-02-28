import mysql.connector
from Config.DB_Config import DB_CONFIG
from Exceptions.DatabaseException import DatabaseException

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(**DB_CONFIG)
                self.cursor = self.connection.cursor()
            except mysql.connector.Error as e:
                raise DatabaseException.db_connect_error(e)
        return self.connection

    def execute(self, query, values=None):
        try:
            self.connect()
            self.cursor.execute(query, values or ())
            self.connection.commit()
        except mysql.connector.Error as e:
            raise DatabaseException.query_execution_error(e)

    def fetchall(self, query, values=None):
        try:
            self.connect()
            self.cursor.execute(query, values or ())
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise DatabaseException.query_execution_error(e)

    def fetchone(self, query, values=None):
        try:
            self.connect()
            self.cursor.execute(query, values or ())
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            raise DatabaseException.query_execution_error(e)

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            self.connection = None
            self.cursor = None
